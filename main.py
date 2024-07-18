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
    buttons=[
                button.inline("США", b"usa"),
                button.inline("УКРАИНА", b"ukr"),
                button.inline("НИДЕРЛАНДЫ", b"ndr"),
                ]
    await event.respond(f'Hello, {first_name} ill help you with finding the capital of city', buttons=buttons)

@client.on(events.CallbackQuery(pattern=b"usa"))
async def nikoglai_answer(event):
    await event.respond("341 mln")


@client.on(events.CallbackQuery(pattern=b"ukr"))
async def nikoglai_answer(event):
    await event.respond("31 mln")


@client.on(events.CallbackQuery(pattern=b"ndr"))
async def nikoglai_answer(event):
    await event.respond("17 mln")



async def main():
    await client.start(bot_token=bot_token)
    await client.run_until_disconnected()


if __name__ == '__main__':
    client.loop.run_until_complete(main())
