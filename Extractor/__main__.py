import asyncio
import importlib
from pyrogram import idle, Client, filters
import logging
from Extractor.modules import ALL_MODULES
from config import API_ID, API_HASH, BOT_TOKEN

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)

loop = asyncio.get_event_loop()

app = Client(
    ":Extractor:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

@app.on_message(filters.command("ping"))
async def ping_handler(client, message):
    await message.reply_text("pong!")

async def sumit_boot():
    try:
        for all_module in ALL_MODULES:
            importlib.import_module("Extractor.modules." + all_module)
        await app.start()
        logging.info("Bot started and connected to Telegram!")
        print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
        await idle()
        print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")
    except Exception as e:
        logging.error(f"Failed to start bot: {e}")
        raise

if __name__ == "__main__":
    loop.run_until_complete(sumit_boot())
