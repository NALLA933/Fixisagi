from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import BadRequest
from shivu import LOGGER
from core.state import *
from core.database import user_collection
from core.utils import to_small_caps, safe

async def guess(update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    if chat_id not in last_characters:
        return await update.message.reply_html("<b>No waifu spawned.</b>")

    guess_text = " ".join(context.args).lower()
    actual = last_characters[chat_id]['name'].lower()

    if guess_text != actual:
        return await update.message.reply_html("<b>Wrong guess ❌</b>")

    first_correct_guesses[chat_id] = user_id

    await user_collection.update_one(
        {"id": user_id},
        {"$push": {"characters": last_characters[chat_id]}},
        upsert=True
    )

    await update.message.reply_text(
        f"🎉 {safe(to_small_caps(actual))} added to your harem!",
        parse_mode="HTML"
    )