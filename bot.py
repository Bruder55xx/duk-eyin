import sys

from src.core import main
from src.deeplchain import _banner, _clear, log,hju,pth,mrh
from keep_alive import keep_alive
import websockets
from loguru import logger
from flask import Flask
# Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

def run_flask():
    app.run(debug=True)


if __name__ == "__main__":
    _clear()
    keep_alive()
    _banner()
    log(hju + f"Please wait, starting your bot...")
    log(pth + "~" * 38)
    while True:
        try:
            main()
        except KeyboardInterrupt:
            log(mrh + f"Successfully logged out of the bot\n")
            sys.exit()
