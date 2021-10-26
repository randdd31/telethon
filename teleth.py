from telethon import TelegramClient
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest, GetInlineBotResultsRequest

# Use your own values from my.telegram.org
api_id = 1141161
api_hash = 'cea6e327693f3d9a366822f3b2b13bf2'

client = TelegramClient('yuda', api_id, api_hash).start(phone=+6285292522292)
async def main():
    bot = await client.get_entity('@akuTubeBot')
    # print(bot,"\n")
    # await client.send_message(bot, '/start')
    message = await client.get_messages(bot, 1)
    messageId = message[0].id
    # print(message[0].message)
    for a in message[0].reply_markup.rows:
        print("\n")
        for b in a.buttons:
            print(f"Text = {b.text}\nData = {b.data}")

    await client(GetBotCallbackAnswerRequest(
        peer=bot,
        msg_id=messageId,
        data=message[0].reply_markup.rows[0].buttons[0].data
    ))
        
with client:
    client.loop.run_until_complete(main())

