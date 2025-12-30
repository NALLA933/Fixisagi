from core.state import *
from logic.spawn import send_spawn
import asyncio

async def message_counter(update, context):
    if update.effective_chat.type not in ("group", "supergroup"):
        return

    chat_id = str(update.effective_chat.id)

    if chat_id not in locks:
        locks[chat_id] = asyncio.Lock()

    async with locks[chat_id]:
        message_counts[chat_id] = message_counts.get(chat_id, 0) + 1

        if message_counts[chat_id] >= MESSAGE_FREQUENCY:
            message_counts[chat_id] = 0
            if not currently_spawning.get(chat_id):
                currently_spawning[chat_id] = True
                asyncio.create_task(send_spawn(update, context))