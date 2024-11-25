import asyncio
import json
from aio_pika import connect, Message
from config.settings import settings

async def send_message(connection, message_data):
    async with connection:
        channel = await connection.channel()
        await channel.default_exchange.publish(
            Message(body=json.dumps(message_data).encode()),
            routing_key='test_queue',
        )
        print("Сообщение отправлено:", message_data)

async def main():
    connection = await connect(settings.rabbit_url)

    await send_message(connection, {"type": "add_to_favorites", "user_id": 1, "meme_uuid": "uuid-123"})
    await send_message(connection, {"type": "open_meme", "meme_uuid": "uuid-123"})

if __name__ == '__main__':
    asyncio.run(main())
