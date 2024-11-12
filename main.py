from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import asyncio

TOKEN = '7447836010:AAHJ7d0IFts0JG4DK_5vgdpMDKxHxBScrM4'
WEB_APP_URL = 'https://maestro2315.github.io/PC_BotTG2/'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    button_cpu = KeyboardButton(text="💻 Процессоры", web_app=WebAppInfo(url=f"{WEB_APP_URL}?item=cpu"))
    button_gpu = KeyboardButton(text="🖥 Видеокарты", web_app=WebAppInfo(url=f"{WEB_APP_URL}?item=gpu"))
    button_motherboard = KeyboardButton(text="🔧 Материнские платы", web_app=WebAppInfo(url=f"{WEB_APP_URL}?item=motherboard"))
    button_ram = KeyboardButton(text="💾 Оперативная память", web_app=WebAppInfo(url=f"{WEB_APP_URL}?item=ram"))
    button_storage = KeyboardButton(text="📀 Накопители", web_app=WebAppInfo(url=f"{WEB_APP_URL}?item=storage"))

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(button_cpu, button_gpu, button_motherboard, button_ram, button_storage)

    await message.answer("Выберите комплектующие для подробной информации:", reply_markup=keyboard)

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
