from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from modules import leveling_system
from modules.commands.exp_command import get_user_exp

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm alive 🧠")


async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await leveling_system.handle_message(update, context)


# Build the bot
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler('exp', get_user_exp))
app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, on_message))

# Run polling
app.run_polling()
