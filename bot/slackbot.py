import os
from pathlib import Path
from dotenv import load_dotenv
from slack import WebClient
from flask import Flask
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events',app)

bot = WebClient(os.environ['SLACK_TOKEN'])
BOT_ID = bot.api_call("auth.test")['user_id']


@slack_event_adapter.on('app_mention')
def message(payload):
    event= payload.get('event',{})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    message = "Hia <@" + user_id + ">, your message was: " + text.replace("<@"+BOT_ID+">","");
    if BOT_ID != user_id:
        bot.chat_postMessage(channel=channel_id, text=message)

if __name__ == '__main__':
    app.run(debug=True)