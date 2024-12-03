from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def generate_main_menu():
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text="📝 Kategoriyalar")
    )
    builder.row(
        KeyboardButton(text="🛒 Savatcha"),
        KeyboardButton(text="📄 Buyutmalar tarixi")
    )
    builder.row(
        KeyboardButton(text="⚙️ Sozlamalar"),
    )

    return builder.as_markup(resize_keyboard=True)
