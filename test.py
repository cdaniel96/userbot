from telethon.sync import TelegramClient
from telethon import events

api_id = 17436972
api_hash = '07137e882a2c8888d9c65407936fa601'
phone = '+16086889935'
client = TelegramClient(phone, api_id, api_hash)
client.start()


@client.on(events.NewMessage(chats=('chtwrsbot')))
async def handler(event):
    if '/go' in event.raw_text:
        await event.reply('/go')


client.run_until_disconnected()
