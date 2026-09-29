from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from handlers import commands_handler
import os

load_dotenv()

TOKEN = os.environ["TOKEN"]
if not TOKEN:
    raise RuntimeError("TOKEN environment variable is not set")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return
    await update.message.reply_text("Salut 👋")

async def post_init(app: Application):
    me = await app.bot.get_me()
    print(f"Connected as @{me.username} | Bot ID: {me.id}")

def create_app():
    app = (
        Application.builder()
        .token(TOKEN)
        .post_init(post_init)
        .build()
    )
    return app

def start_app(app):
    commands_handler.handle_commands(app)
    app.run_polling()

def main():
    print("Initializing the bot...")

    app = create_app()
    start_app(app)
    

if __name__ == "__main__":
    main()