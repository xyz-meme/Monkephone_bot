 import logging
from dotenv import load_dotenv
load_dotenv()

import os
import random
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Enable logging
logging.basicConfig(level=logging.INFO)

# Bot token
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN is missing in environment variables!")

# ----- Command: /start -----
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "☎️ Welcome to *MonkePhone Bot*!\nType /call to hear from the monke.\nType /rules to survive the jungle.",
        parse_mode='Markdown'
    )

# ----- Command: /rules -----
async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📜 *Group Rules:*\n1. No paper hands\n2. No FUD\n3. Obey the phone 📞\n4. Memes = life",
        parse_mode='Markdown'
    )

# ----- Command: /call -----
async def call(update: Update, context: ContextTypes.DEFAULT_TYPE):
    messages = [
        "☎️ Monke says: Buy the top, regret the bottom.",
        "📉 It’s not a dump, it’s stealth accumulation.",
        "🚀 The moon called — they’re full. Next rocket is Monke-only.",
        "🦍 Hold tight. Bananas don't sell themselves.",
    ]
    await update.message.reply_text(random.choice(messages))

# ----- Welcome New Members -----
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"👋 Welcome {member.first_name} to *MonkeLand*!\n📞 Type /rules or /call to begin the journey.",
            parse_mode='Markdown'
        )

# ----- Auto Reply -----
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text.lower()
    triggers = ["moon", "dump", "rug", "rekt", "paper", "scam", "gm", "gn"]
    if any(word in user_msg for word in triggers):
        responses = [
            "📞 Hold the line. Monke is watching.",
            "💎 Only weak hands fear the red.",
            "🚀 This is just a dip before the rip.",
            "🧠 Don't let your brain override the phone.",
        ]
        await update.message.reply_text(random.choice(responses))

# ----- Main Entry -----
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("rules", rules))
    app.add_handler(CommandHandler("call", call))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    logging.info("🤖 MonkePhone Bot is now running...")
    app.run_polling()
