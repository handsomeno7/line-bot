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

line_bot_api = LineBotApi('WLDgWWdPrfzX2/0PqF0Lx4sxMCWH993mR6/PiweTxf/mvAeDuKXpr44G1/MDHJ8UjW2QbDwNHN/AcRb8UfFfYhnj2pa0J9HNulJhKVHiMHkdXNza4ZJc1V+EnT1jbch3bOEHuOb4aKtpfOzZeOjyTQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e01db9e1dc0396b2a0b2b2455643484c')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '你在公三小'

    if msg == 'hi':
        r = '您好'
    elif msg == 'hello':
        r = 'yo man'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()