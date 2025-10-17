from user import User

users = {}

xp_table = {
    'text': 1,
    'photo': 5,
    'sticker': 2,
    'voice': -4
}

async def handle_message(update, context):
    user_id = update.effective_user.id
    name = update.effective_user.first_name 

    if user_id not in users:
        users[user_id] = User(user_id, name)

    user = users[user_id]

    # Detect message type and assign XP
    exp_gain = next(
        (xp for attr, xp in xp_table.items() if getattr(update.message, attr, None)),
        0
    )

    result = user.exp_handler(exp_gain)

    # Send feedback
    if result == "level_up":
        await update.message.reply_text(f"🎉 {user.name} reached Level {user.level}!")
    elif result == "level_down":
        await update.message.reply_text(f"⬇️ {user.name} dropped to Level {user.level}...")
