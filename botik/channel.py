import asyncio
import os
import requests
from bs4 import BeautifulSoup
from random import choice
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from loguru import logger
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
CHANNEl_ID = os.getenv("CHANNEL_ID")


async def send_jokes_task(bot: Bot):
    while True:
        try:
            response = requests.get("https://t.me/BanChanKristofer1234_bot")
            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')
                jokes = soup.find.all('div', class_='text')
                joke = choice(jokes).text.strip()
                await bot.send_message(CHANNEl_ID, f"Анекдот:\n{joke}")
                logger.success("Канал: анекдот отправлен!")
            else:
                logger.warning("Канал: проблема с сайтом!")
        except Exception as e:
            logger.error(f"Канал: ошибка! {e}")


def setup_channel_handlers(dp: Dispatcher, bot: Bot):
    asyncio.create_task(send_jokes_task(bot))

    @dp.message(Command('channel_stats'), F.chat.type == "channel")
    async def channel_stats(message: types.Message):
        await message.answer("Бот канала работает!")
        logger.info("Канал: проверка работы")
