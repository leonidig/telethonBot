from telethon import TelegramClient, events
from telethon.tl.custom import Button as button
from os import getenv


api_id = getenv("api_id")
api_hash = getenv("api_hash")
bot_token = getenv("bot_token")


client = TelegramClient('bot_session', api_id, api_hash)


@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    sender = await event.get_sender()
    first_name = sender.first_name
    buttons = [
            button.text("Ukraine", resize=True),
            button.text("USA", resize=True),
            button.text("Netherlands", resize=True)
        ]
    await event.respond(f'Hello, {first_name} ill help you with finding the capital of city', buttons=buttons)


@client.on(events.NewMessage(pattern='Ukraine'))
async def handler_some1(event):
    await event.respond('Capital of Ukraine - Kiev')

@client.on(events.NewMessage(pattern='USA'))
async def handler_some1(event):
    await event.respond('Capital of USA - Washington')

@client.on(events.NewMessage(pattern='Netherlands'))
async def handler_some1(event):
    await event.respond('Capital of Netherlands - Amsterdam')


async def main():
    await client.start(bot_token=bot_token)
    await client.run_until_disconnected()


if __name__ == '__main__':
    client.loop.run_until_complete(main())
