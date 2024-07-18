from telethon import TelegramClient, events
from telethon.tl.custom import Button as button
from telethon.events import CallbackQuery
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
                button.inline("Ukraine", b"ukraine"),
            ]

    await event.reply(f'Hello, {first_name} ill help you with finding the capital of city', buttons=buttons)
    reply_buttons = [
            # button.request_phone
            button.text("Support", resize=True)
        ]
    await event.reply("Or you can wrote to our supporter", buttons=reply_buttons)




@client.on(events.CallbackQuery)
async def enter_city_data(event):
    if event.data == b'ukraine':
        inline_buttons = [
            [button.inline("Odessa", b"odessa")],
            [button.inline("Kharkov", b"kharkov")],
            [button.inline("Lvov", b"lvov")],
            [button.inline("Kyiv", b"kyiv")],
            [button.inline("Dnepropetrovsk", b"dnepropetrovsk")]
        ]

        await event.respond('Okey, please choose city', buttons=inline_buttons)
    if event.data == b"odessa":
        await event.respond("• Area: 236.9 km²\n• Population: 1 mln (2023)\n• Ukraine's largest port, an important centre of trade and transport\n• There are 2,500 kilometres of catacombs under the city.They were used by partisans in WWII.")
    if event.data == b"kharkov":
        await event.respond("• Area: 350 km²\n• Population: 1.4 mln (2023)\n• Major industrial, cultural, and educational centre\n• Home to Ukraine's oldest university, founded in 1804\n• Renowned for its Freedom Square, one of the largest city squares in Europe\n• Significant transport hub with an extensive metro system\n• Rich architectural heritage, including constructivist buildings")
    if event.data == b"lvov":
        await event.respond("• Area: 182 km²\n• Population: 720,000 (2023)\n• Important cultural, historical, and economic centre\n• Known for its well-preserved architecture and historic buildings\n• UNESCO World Heritage site due to its old town\n• Home to many universities, theatres, and museums\n• Famous for its coffee culture and annual festivals")
    if event.data == b"kyiv":
        await event.respond("• Area: 839 km²\n• Population: 2.9 mln (2023)\n• Capital and largest city of Ukraine\n• Major political, cultural, and economic centre\n• Home to numerous historical landmarks, including Kyiv Pechersk Lavra\n• Known for its vibrant arts scene and nightlife\n• Important educational hub with many universities")
    if event.data == b"dnepropetrovsk":
        await event.respond("• Area: 405 km²\n• Population: 1 mln (2023)\n• Major industrial and business centre\n• Important transportation hub with a significant river port\n• Known for its aerospace and manufacturing industries\n• Home to several universities and research institutions\n• Renowned for its long embankment along the Dnieper River")
    else:
        await event.answer("Erorr, please try again")


@client.on(events.NewMessage(pattern="Support"))
async def support(event):
    await event.respond("You can write our suppoerter @big_pencil19")


async def main():
    await client.start(bot_token=bot_token)
    await client.run_until_disconnected()


if __name__ == '__main__':
    client.loop.run_until_complete(main())
