from shivu import db, LOGGER
from pymongo import collection as pymongo_collection
from pymongo.errors import OperationFailure

# Collections
collection = db['anime_characters']
user_collection = db['users']
user_totals_collection = db['user_totals']
group_user_totals_collection = db['group_user_totals']
top_global_groups_collection = db['top_global_groups']

# ---- MongoDB index crash fix ----
_orig_create_index = pymongo_collection.Collection.create_index

def _safe_create_index(self, keys, **kwargs):
    try:
        return _orig_create_index(self, keys, **kwargs)
    except OperationFailure as e:
        if e.code == 86:
            LOGGER.debug(f"Index already exists on {self.name}")
            return None
        raise

pymongo_collection.Collection.create_index = _safe_create_index


async def fix_indexes():
    try:
        await collection.drop_index("id_1")
        await collection.drop_index("characters.id_1")
        LOGGER.info("✅ DB indexes cleaned")
    except Exception:
        LOGGER.info("ℹ️ Index cleanup not required")