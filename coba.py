from telethon import TelegramClient, events, errors
import re
from time import sleep

api_id = 1141161
api_hash = 'cea6e327693f3d9a366822f3b2b13bf2'

client = TelegramClient('yuda', api_id, api_hash).start(phone=+6285292522292)
async def main():
    peer = await client.get_entity('https://t.me/joinchat/rYrrj5zF14FhZTBl')
    peer2 = await client.get_entity("https://t.me/SignificantTrades")
    messages = await client.get_messages(peer2, 50)
    for message in messages:
        messageId = message.id
        message = re.split("\n+", message.message)
        for a in message:
            sleep(1)
            if float(re.split(" +", a)[2].split('$')[1].split('M')[0]) > 10:
                try:
                    # await client.forward_messages(peer, messageId, peer2)
                    await client.send_message(peer, a)
                    print("ya")
                except IndexError:
                    print(a)
            else:
                print(f"no")



with client:
    client.loop.run_until_complete(main())
