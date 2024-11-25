import asyncio
import json
import asyncpg
from aio_pika import connect, IncomingMessage
from config.settings import settings

DB_CONFIG = {
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database',
    'host': 'localhost'
}

async def get_db_connection():
    return await asyncpg.connect(**DB_CONFIG)

async def on_message(message: IncomingMessage):
    async with message.process():
        print('Получено сообщение: {}'.format(message.body))
        try:
            message_data = json.loads(message.body)
            message_type = message_data.get("type")

            async with get_db_connection() as conn:
                if message_type == "add_to_favorites":
                    await add_to_favorites(conn, message_data)
                elif message_type == "open_meme":
                    await open_meme(conn, message_data)
                else:
                    print(f"Неизвестный тип сообщения: {message_type}")

        except json.JSONDecodeError:
            print("Ошибка декодирования JSON")

async def add_to_favorites(conn, data):
    user_id = data['user_id']
    meme_uuid = data['meme_uuid']
    await conn.execute('''
        INSERT INTO baskets (user_uuid, meme_uuid) VALUES ($1, $2)
        ON CONFLICT (user_uuid, meme_uuid) DO NOTHING;
    ''', user_id, meme_uuid)
    print(f"Мем {meme_uuid} добавлен в избранное пользователю {user_id}.")

async def open_meme(conn, data):
    meme_uuid = data['meme_uuid']
    meme_info = await conn.fetchrow('''
        SELECT * FROM memes WHERE uuid = $1;
    ''', meme_uuid)
    
    if meme_info:
        print(f"Информация о меме {meme_uuid}: {dict(meme_info)}")
    else:
        print(f"Мем с UUID {meme_uuid} не найден.")

async def main():
    connection = await connect(settings.rabbit_url)
    
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("test_queue", durable=True)

        await queue.consume(on_message)
        print("Ожидание сообщений. Для выхода нажмите CTRL+C")
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
