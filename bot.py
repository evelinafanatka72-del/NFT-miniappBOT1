import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Твой токен и ссылка на Mini App
TOKEN = "8641940120:AAGOtkjQLfMVeVflplgamEPV2KCofMjdIsY"
MINI_APP_URL = "https://evelinafanatka72-del.github.io/NFT-miniappBOT1/"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # Создаем кнопку, которая открывает твой сайт на GitHub прямо в Telegram
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="Открыть мини-приложение", 
        web_app=WebAppInfo(url=MINI_APP_URL))
    )
    
    # Отправляем приветствие
    await message.answer(
        f"Здравствуйте, {html.bold(message.from_user.full_name)}!\n"
        "Откройте мини-приложение, для взаимодействия с ботом.",
        reply_markup=builder.as_markup()
    )

async def main() -> None:
    # Настраиваем бота
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    print("Бот запущен и работает через GitHub Actions!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен")
