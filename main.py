from telethon import TelegramClient, events, Button
import sqlite3
from os import getenv

# Параметры аутентификации
api_id = int(getenv("api_id"))
api_hash = getenv("api_hash")
bot_token = getenv("bot_token")

# Создание и настройка клиента Telegram
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# Функция для создания базы данных и таблицы
def create_db():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        phone_number TEXT,
        first_name TEXT,
        last_name TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

# Вызов функции для создания базы данных и таблицы
create_db()

# Функция для сохранения контакта в базу данных
def save_contact(user_id, phone_number, first_name, last_name):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO contacts (user_id, phone_number, first_name, last_name)
    VALUES (?, ?, ?, ?)
    ''', (user_id, phone_number, first_name, last_name))
    
    conn.commit()
    conn.close()

# Обработчик команды /start
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    buttons = [
        [Button.request_phone('Send your contact')]
    ]
    await event.respond('Please send me your contact information:', buttons=buttons)


@client.on(events.NewMessage)
async def handle_message(event):
    if event.message.contact:
        contact = event.message.contact
        save_contact(contact.user_id, contact.phone_number, contact.first_name, contact.last_name)
        await event.respond('Contact saved successfully!')

# Основная функция для запуска клиента
async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
