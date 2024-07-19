from telethon import TelegramClient, events, Button
import sqlite3
from os import getenv

# Параметры аутентификации
api_id = getenv("api_id")
api_hash = getenv("api_hash")
bot_token = getenv("bot_token")

# Создание и настройка клиента Telegram
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

def create_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER DEFAULT 0,
            phone_number TEXT DEFAULT NULL,
            first_name TEXT DEFAULT NULL,
            last_name TEXT DEFAULT NULL
        )
    """)
    conn.commit()
    conn.close()

# Вызов функции для создания базы данных и таблицы
create_db()

def save_contact(user_id, phone_number, first_name, last_name):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO contacts (user_id, phone_number, first_name, last_name)
    VALUES (?, ?, ?, ?)
    ''', (user_id, phone_number, first_name, last_name))

    conn.commit()
    conn.close()

def find_contacts_by_first_name(search_name):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM contacts
    WHERE first_name = ?
    ''', (search_name,))

    results = cursor.fetchall()
    conn.close()
    return results

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    buttons = [
        [Button.request_phone('Send your contact')]
    ]
    await event.respond('Please send me your contact information:', buttons=buttons)

@client.on(events.NewMessage())
async def handle_message(event):
    if event.message.contact:
        contact = event.message.contact
        user_id = contact.user_id
        phone_number = contact.phone_number
        first_name = contact.first_name
        last_name = contact.last_name

        save_contact(user_id, phone_number, first_name, last_name)

        search_name = 'QWERTY'
        results = find_contacts_by_first_name(search_name)

        if results:
            message = f"Found contacts with name {search_name}:\n" + '\n'.join([f'ID: {row[0]}, Name: {row[3]}, Phone: {row[2]}' for row in results])
        else:
            message = f'No contacts found with the name "{search_name}".'

        await event.respond(message)

async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
