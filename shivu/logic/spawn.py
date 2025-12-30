import asyncio, random, traceback
from telegram.error import BadRequest
from shivu import LOGGER
from core.state import *
from core.database import collection
from html import escape

async def despawn_character(chat_id, message_id, character, context):
    await asyncio.sleep(DESPAWN_TIME)

    if chat_id in first_correct_guesses:
        cleanup(chat_id)
        return

    try:
        await context.bot.delete_message(chat_id, message_id)
    except BadRequest:
        pass

    caption = f"""⏰ Time's up!

🧸 <b>{escape(character['name'])}</b>
📺 <b>{escape(character['anime'])}</b>
🎯 <b>{escape(character['rarity'])}</b>
"""

    try:
        await context.bot.send_photo(
            chat_id,
            character['img_url'],
            caption=caption,
            parse_mode="HTML"
        )
    except Exception:
        pass

    cleanup(chat_id)


def cleanup(chat_id):
    last_characters.pop(chat_id, None)
    spawn_messages.pop(chat_id, None)
    spawn_message_links.pop(chat_id, None)
    currently_spawning.pop(chat_id, None)