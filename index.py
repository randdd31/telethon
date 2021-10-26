from telethon import TelegramClient, events
import re
from time import sleep

api_id = 1141161
api_hash = 'cea6e327693f3d9a366822f3b2b13bf2'

client = TelegramClient('yuda', api_id, api_hash).start(phone=+6285292522292)
# 1467798247
# chats=1467798247
@client.on(events.NewMessage(chats=1467798247))
async def main(event):
    # peer = await client.get_entity('https://t.me/joinchat/rYrrj5zF14FhZTBl')
    # peer2 = await client.get_entity("https://t.me/SignificantTrades")
    # print(peer)
    peer = 1568573025
    message = re.split("\n+", event.message.message)
    for a in message:
        try:
            sp = re.split(" +", a)[2].split('$')[1].split('M')[0]
            if float(sp) > 10:
                try:
                    await client.send_message(peer, a)
                    print("ya")
                except:
                    print(a)
            else:
                print(f"no  > {a}")

        except:
            continue
    

client.run_until_disconnected()