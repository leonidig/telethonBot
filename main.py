from telethon import TelegramClient, events, Button as button


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
        [button.text("Випадкова порада", resize=True)],
        [button.text("Часті запитання", resize=True)],
        [button.text("Тренери", resize=True)]
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
        await event.respond("Ось всі наші акаунти інстаграм ->")
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


@client.on(events.NewMessage(pattern="Часті запитання"))
async def faq(event):
    await event.respond(
        "Оберіть запитання",
        buttons=[
            [button.inline("Що взяти на тренування", b"workout_gear")],
            [button.inline("Яка частота тренувань оптимальна для новачка?", b'training_frequency')],
            [button.inline("Які додаткові послуги ви надаєте?", b"other_services")]
        ]
    )

@client.on(events.CallbackQuery)
async def answer_faq(event):
    if event.data == b"workout_gear":
        await event.respond('''
Список речей які варто взяти на тренування
• Змінне взуття - спортивні кросівки чи кеди
• Вода - не треба більше 0.75л
• Рушник - чистота залу та особиста гігієна
• Змінна одежа - не забудьте взяти змінний одяг для комфортного перебування після тренування 
З цим списком речей ви будете комфортно почувати себе у спорт-залі
Бажаємо успіхів 🏆                        
''')
    if event.data == b"training_frequency":
        await event.respond("Для новачка 2 рази на тиждень буде непоганим результатом.\nЯкщо ви вже більш на продвинутому рівні — 3 рази.\n4 рази на тиждень, якщо ви вже досягли високих результатів і хочете підтримувати або покращувати свою фізичну форму.")
    if event.data == b'other_services':
        await event.respond("Окрім тренувань ми пропонуємо вам -\n- Групові заняття стречінгом\n- Масажні процедури\n- Пробіжки у групах")



@client.on(events.NewMessage(pattern="Тренери"))
async def send_coach(event):
    await event.respond("Оберіть тренера",
    buttons = [
        button.text("Жора"),
        button.text("Марія"),
        button.text("Олег"),
        button.text("Катя"),
        button.text("Дмитро"),
    ])

@client.on(events.NewMessage)
async def answer_coach(event):
    jora_path = '/Users/leonidlisovskiy/Desktop/telethonBot/telethonBot-2/imgs/jora.jpg'
    marisha_path = '/Users/leonidlisovskiy/Desktop/telethonBot/telethonBot-2/imgs/marisha.jpg'
    oleg_path = '/Users/leonidlisovskiy/Desktop/telethonBot/telethonBot-2/imgs/oleg.jpg'
    katya_path = '/Users/leonidlisovskiy/Desktop/telethonBot/telethonBot-2/imgs/katya.jpg'
    dima_path = '/Users/leonidlisovskiy/Desktop/telethonBot/telethonBot-2/imgs/dima.jpg'

    if event.message.message == "Жора":
        await event.respond("Жора 💪")
        await client.send_file(event.chat_id, jora_path, caption='',
        buttons= [button.url("Інстаграм Жори", "https://www.instagram.com/jora_hajime?igsh=M3BibjdqaTB3b29s")])
    elif event.message.message == "Марія":
        await event.respond("Марія 🌹")
        await client.send_file(event.chat_id, marisha_path, caption='',
        buttons= [
                [button.url("Інстаграм Марії", "https://www.instagram.com/marisha_grechechka?igsh=ZjcxNTVxd2I0NHZ4")],
                [button.url("Тік-Ток Марії", "https://www.tiktok.com/@mariagrechechka?_t=8oCycQUk59K&_r=1")]
            ])
    elif event.message.message == "Олег":
        await event.respond("Олег 🏅")
        await client.send_file(event.chat_id, oleg_path, caption='',
        buttons=[
            [button.url("Інстаграм Олега", "https://www.instagram.com/oleg_kirlan?igsh=MWF4bzc2MGN2ZnoyNQ==")]
        ])
    elif event.message.message == "Катя":
        await event.respond("Катя 🌺")
        await client.send_file(event.chat_id, katya_path, caption='',
        buttons= [
            [button.url("Інстаграм Каті", "https://www.instagram.com/ekgera_fit_coach?igsh=ZWZ2Z20ya2d4N3R4")],
            [button.url("Тік-Ток Каті", "https://www.tiktok.com/@_gera46_?_t=8lzmC7nSgP0&_r=1&fbclid=PAZXh0bgNhZW0CMTEAAaYgnt-ECrYB5NFWDEPYGR5KZWx09Ha-47NOW6FHwaPJzCWWCvQ4ZO8STrw_aem_t8efuA6M9Vj3SOuUS1lr3Q")]
        ]                       )
    elif event.message.message == "Дмитро":
        await event.respond("Дмитро ⚡")
        await client.send_file(event.chat_id, dima_path, caption='',
        buttons=[
            [button.url("Інстаграм Дмитра", "https://www.instagram.com/grek0036?igsh=czJwcG8yZGw5bHBw")]
        ])



async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())