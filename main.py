from telethon import TelegramClient, events, Button as button
from telethon.tl.types import InputPhoneContact
import sqlite3
from os import getenv


api_id = getenv("api_id")
api_hash = getenv("api_hash")
bot_token = getenv("bot_token")


client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    reply_buttons = [
        [button.text("Coц-мережи", resize=True)],
        [button.text("Адреси", resize=True)],
        [button.text("Прайс-ліст", resize=True)]
    ]
    await event.respond("Привіт, я бот Rio Fitness Club 🤖", buttons = reply_buttons)

@client.on(events.NewMessage(pattern="Coц-мережи"))
async def send_social_networks(event):
    all_social_networks = [
                [button.inline("Інстаграм", b"instagram")],
                [button.inline("Фейсбук", b"facebook")],
                [button.inline("Тік-Ток", b"tiktok")]
    ]
    await event.respond("Тільки підпишись 🥇",buttons = all_social_networks)

@client.on(events.CallbackQuery)
async def enter_social_link(event):
    if event.data == b"instagram":
        await event.respond("Ось всі наші акаунти ->")
        rio_fitness_btn = [button.url("Клік", "https://www.instagram.com/rio_fitness_club")]
        await event.respond("Наш Інстаграм", buttons = rio_fitness_btn)
        rio_school_btn = [button.url("Клік", "https://www.instagram.com/rioschool")]
        await event.respond("Також можеш перейти до нашої rioschool", buttons=rio_school_btn)

    elif event.data == b"facebook":
        await event.respond("Наш Facebook")
        rio_facebook_btn = [button.url("Жмак", "https://www.facebook.com/FitnessRioClub")]
        await event.respond("Залітай ->", buttons = rio_facebook_btn)

    elif event.data == b"tiktok":
        await event.respond("Tik - Tok акаунт")
        rio_tiktok_btn = [button.url("Нажми мене", "https://www.tiktok.com/@rio_fitness_club0")]
        await event.respond("Погротай Наш Тік-Ток", buttons = rio_tiktok_btn)



@client.on(events.NewMessage(pattern="Адреси"))
async def send_addresses(event):
    all_addresses = [
        [button.inline("Ріо Фітнес - 1", b"rio_1")],
        [button.inline("Ріо Фітнес - 2", b"rio_2")],
        [button.inline("Ріо Фітнес - 3", b"rio_3")],
        [button.inline("Ріо Фітнес - 4", b"rio_4")],
        [button.inline("Ріо Фітнес - 5", b"rio_5")],
        [button.inline("Ріо Фітнес - 6", b"rio_6")]
    ]
    await event.respond("Вибери потрібну адресу: ", buttons = all_addresses)


contact = InputPhoneContact(
        client_id=0,
        phone= '0639658039',
        first_name= "Rio Number",
        last_name= None
    )
@client.on(events.CallbackQuery)
async def enter_data_club(event):

    if event.data == b'rio_1':
        await event.respond("• Rio Fitness Club №1\n•Адреса - вулиця Космонавтів, 62/2, Одеса, Одеська область, 65000\n• Розклад Пн - Сб : 08.00 : 22.00")
        await event.respond('Контактний номер', contact)


async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())