from telethon import TelegramClient, events, Button as button
from telethon.tl.types import InputMediaContact
import sqlite3
from os import getenv
from random import choice


api_id = getenv("api_id")
api_hash = getenv("api_hash")
bot_token = getenv("bot_token")


client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    reply_buttons = [
        [button.text("Coц-мережи", resize=True)],
        [button.text("Адреси", resize=True)],
        [button.text("Прайс-ліст", resize=True)],
        [button.text("Випадкова порада", resize=True)]
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




@client.on(events.CallbackQuery)
async def enter_data_club(event):
    if event.data == b'rio_1':
        await event.respond("• Rio Fitness Club №1\n•Адреса - вулиця Космонавтів, 62/2, Одеса\n• Розклад Пн - Сб : 08.00 : 22.00 ; Нд - вихідний\n" + "• Контактиний номер +380639658039")
    if event.data == b'rio_2':
        await event.respond("• Rio Fitness Club №2\n• Адреса - вулиця Академіка Корольова, 7, Одеса\n• Розклад Пн - Сб : 08.00 : 22.00 ; Нд - 11.00 : 16.00\n" + "• Контактиний номер +380954424913")
    if event.data == b'rio_3':
        await event.respond("• Rio Fitness Club №3\n•Адреса - вулиця Радісна вулиця, 15, Одеса\n• Розклад Пн - Сб : 08.00 : 22.00 ; Нд - вихідний\n" + "• Контактиний номер +380639962059")
    if event.data == b'rio_4':
        await event.respond("• Rio Fitness Club №4\n•Адреса - вулиця Семена Палія, 93А, Одеса\n• Розклад Пн - Сб : 08.00 : 22.00 ; Нд - 11.00 : 16.00\n" + "• Контактиний номер +380937505878")
    if event.data == b'rio_5':
        await event.respond("• Rio Fitness Club №5\n•Адреса - вулиця Торгова 2 с/2ш-2, Чорноморськ, Одеська область\n• Розклад Пн - Сб : 08.00 : 22.00 ; Нд - 11.00 : 16.00\n" + "• Контактиний номер +380637437500")
    if event.data == b'rio_6':
        await event.respond("Скоро!\nНаразі Rio Fitness Club №6 перебуває у стадії будівництва.")



@client.on(events.NewMessage(pattern="Прайс-ліст"))
async def send_price_list(event):
    
    await event.respond('''
• Перше тренування - 0 грн
• 400грн (до 15 років) - місяць
• 580грн після 15 - місяць
• 1400 після 15 років за 3 місяці
• 2550грн з тренером - місяць
''')

tips = ["Розминка перед тренуванням", "Пийте достатньо води", "Слідкуйте за технікою виконання вправ", "Поступово збільшуйте навантаження", "Використовуйте різноманітні вправи", "Слухайте своє тіло", "Правильне харчування", "Відпочивайте між підходами", "Використовуйте належне спортивне обладнання", "Слідкуйте за диханням", "Тренуйте всі групи м'язів", "Записуйте свої результати", "Займайтеся з тренером", "Робіть стретчинг", "Не забувайте про кардіо", "Слідкуйте за поставою", "Плануйте свої тренування", "Відпочивайте достатньо", "Не перевантажуйтеся", "Використовуйте додаткові аксесуари", "Контролюйте вагу","Слідкуйте за своїм станом здоров'я", "Мотивуйте себе", "Залучайте друзів", "Насолоджуйтеся процесом"]

@client.on(events.NewMessage(pattern="Випадкова порада"))
async def send_tip(event):
    recomend_tip = choice(tips)
    tip_btn = [
        button.inline("Ще порада!", b'next_tip')
    ]
    await event.respond(f"Ваша порада - {recomend_tip}", buttons=tip_btn)

@client.on(events.CallbackQuery(pattern=b"next_tip"))
async def tip_answer(event):
    recomend_tip = choice(tips)
    tip_btn = [
        button.inline("Ще порада!", b'next_tip')
    ]
    await event.edit(f"Ваша порада - {recomend_tip}", buttons=tip_btn)




async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
