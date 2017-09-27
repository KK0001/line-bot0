import os
from replys.reply_comments import *
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


app = Flask(__name__)

# 環境変数
channel_secret = os.environ['CSecret']
channel_access_token = os.environ['AToken']

# 環境変数が無い場合
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

# インスタンス
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    t = event.message.text

    # おはよ
    # if((t=='おは')||(t=='おはよー')||(t=='おはよ')):
    if(t=='おは'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=ohayo()))

    # おやす
    if(t=='おやす'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=oyasu()))

    if(t=='ん'):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='ん！'))

    # その他、テキトーに返信
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=auto_reply()))


if __name__ == "__main__":
    app.run()
