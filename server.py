from flask import Flask
from threading import Thread
import os
from bot import app

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "🤖 Telegram bot is running!"

def run_bot():
    app.run_polling()

if __name__ == "__main__":
    # Runs bot in a separate thread
    Thread(target=run_bot).start()

    # Run Flask on port Render expects
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)
