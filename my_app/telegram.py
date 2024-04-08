import asyncio
from aiogram import Bot, Dispatcher, types

async def get_chat_ids(bot_token):
    bot = Bot(token=bot_token)
    updates = await bot.get_updates()
    chat_ids = [update.message.chat.id for update in updates if update.message.chat.id is not None]
    return chat_ids


async def send_message(bot_token, chat_id, text):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=text)


async def send_to_all(bot_token, text):
    chat_ids = await get_chat_ids(bot_token)
    for chat_id in chat_ids:
        await send_message(bot_token, chat_id, text)


# Test qilish
async def send_sms(text):
    bot_token = '7199036679:AAHBM6wDGLha-6Kyb-PojeuSsFyKiDqn500'
    await send_to_all(bot_token, text)