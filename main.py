from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import asyncio

TOKEN = '7447836010:AAHJ7d0IFts0JG4DK_5vgdpMDKxHxBScrM4'
WEB_APP_URL = 'https://maestro2315.github.io/PC_BotTG2/'  # Замените на ваш URL с GitHub Pages

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Создаем кнопки с иконками
    web_app_button_1 = KeyboardButton(text="💻 Процессоры", web_app=WebAppInfo(url=f"{WEB_APP_URL}?item=cpu"))
    web_app_button_2 = KeyboardButton(text="🖥 Видеокарты", web_app=WebAppInfo(url=f"{WEB_APP_URL}?item=gpu"))
    web_app_button_3 = KeyboardButton(text="🔧 Материнские платы", web_app=WebAppInfo(url=f"{WEB_APP_URL}?item=motherboard"))
    web_app_button_4 = KeyboardButton(text="💾 Оперативная память", web_app=WebAppInfo(url=f"{WEB_APP_URL}?item=ram"))
    web_app_button_5 = KeyboardButton(text="📀 Накопители", web_app=WebAppInfo(url=f"{WEB_APP_URL}?item=storage"))

    # Создаем клавиатуру в один столбец по центру
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(web_app_button_1, web_app_button_2, web_app_button_3, web_app_button_4, web_app_button_5)

    # Отправляем сообщение с кнопками
    await message.answer(
        "Выберите комплектующие для получения подробной информации:",
        reply_markup=keyboard
    )

async def main():
    # Запуск бота
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
