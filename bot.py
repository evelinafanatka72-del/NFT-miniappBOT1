import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

# ДАННЫЕ
TOKEN = "DID YOU REALLY HOPE TO STEAL THE TOKEN? FUCK YOU!"
MINI_APP_URL = "https://evelinafanatka72-del.github.io/NFT-miniappBOT1/"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="💎 Открыть NFT-Маркет", 
        web_app=WebAppInfo(url=MINI_APP_URL))
    )
    
    await message.answer(
        f"Привет, {html.bold(message.from_user.full_name)}!\n\n"
        "🔥 Добро пожаловать в систему внутренних NFT.\n"
        "💰 Здесь ты можешь создавать и покупать активы.",
        reply_markup=builder.as_markup()
    )

async def main() -> None:
    # Используем подавление ошибок сессии
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    logging.info("Бот запускается...")
    try:
        # skip_updates=True поможет, если бот долго лежал и накопил гору спама
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    while True: # Цикл для автоматического перезапуска при падении
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            break
        except Exception as e:
            logging.error(f"Рестарт после ошибки: {e}")
            continue
