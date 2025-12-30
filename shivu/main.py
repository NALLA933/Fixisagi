import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from shivu import application, shivuu, LOGGER
from core.database import fix_indexes
from logic.guess import guess
from handlers.message_counter import message_counter

async def main():
    await fix_indexes()
    await shivuu.start()

    application.add_handler(CommandHandler(["grab", "g"], guess))
    application.add_handler(MessageHandler(filters.ALL, message_counter))

    await application.initialize()
    await application.start()
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())