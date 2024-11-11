


from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

# URL вашего веб-приложения
WEB_APP_URL = "http://localhost:8000"  # Замените на реальный URL


async def start(update: Update, context: CallbackContext):
    # Создаем клавиатуру с кнопкой для открытия веб-приложения
    keyboard = [
        [
            InlineKeyboardButton("Открыть веб-приложение с комплектующими", web_app=WebAppInfo(url=WEB_APP_URL))
        ]
    ]

    # Создаем разметку для кнопки
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопкой
    await update.message.reply_text(
        "Привет! Нажми кнопку ниже, чтобы открыть веб-приложение с комплектующими для ПК.",
        reply_markup=reply_markup
    )


def main():
    # Указываем токен бота
    application = Application.builder().token("7447836010:AAHJ7d0IFts0JG4DK_5vgdpMDKxHxBScrM4").build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()


if __name__ == '__main__':
    main()
