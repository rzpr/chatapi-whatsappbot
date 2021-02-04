from flask import Flask, request
from wabot import WABot
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Status Online"


@app.route('/home', methods=['POST'])
def home():
    if request.method == 'POST':
        bot = WABot(request.json)
        return bot.processing()

if(__name__) == '__main__':
    app.run(host="localhost", port=8080, debug=True)


