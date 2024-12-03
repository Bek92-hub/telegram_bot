from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

from loader import db

def generate_settings_menu(telegram_id):
    user = db.get_user(telegram_id)  # { "id": 1, "name": "...", "is_subscribed": 1, ... }
    is_subscribed = user.get("is_subscribed") == 1

    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text=f"Obunani {'ochirish' if is_subscribed else 'yondirish'}"),
        KeyboardButton(text="Manzilni kiritish/yangilash"),
    )
    builder.row(
        KeyboardButton(text="👈 Bosh menyu"),
    )

    return builder.as_markup(resize_keyboard=True)
