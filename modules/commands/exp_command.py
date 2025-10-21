from telegram import Update
from telegram.ext import ContextTypes
from modules import leveling_system


async def get_user_exp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in leveling_system.users:
        await update.message.reply_text(
            'Старенький, ти ще не такий крутий, щоб мати рівень'
        )
        return

    user = leveling_system.users[user_id]
    xp_to_next = (user.level * 10) - user.exp
    await update.message.reply_text(
        f'XP: {user.exp}, Рівень: {user.level}, {xp_to_next} XP до наступного рівня.'
    )
