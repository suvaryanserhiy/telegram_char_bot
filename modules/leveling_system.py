from user import User
from data_manager import save_data, load_data
users = {}

xp_table = {
    'text': 1,
    'photo': 5,
    'sticker': 2,
    'voice': -4
}

#Load existing users

_loaded_data = load_data();

for uid, info in _loaded_data.items():
    users[int(uid)] = User(int(uid), info["name"])
    users[int(uid)].level = info["level"]
    users[int(uid)].exp = info["exp"]

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
    
    #Save user
    save_data({uid: vars(u) for uid, u in users.items()})

    # Send feedback
    if result == "level_up":
        await update.message.reply_text(f"🎉 {user.name} досягнув/ла {user.level} рівня!")
    elif result == "level_down":
        await update.message.reply_text(f"⬇️ {user.name} впав/ла до {user.level} рівня...")
