from aiogram.types import Message
from aiogram import F

from router import router
from loader import db
from keyboards.reply.settings import generate_settings_menu


@router.message(F.text == "Obunani ochirish")
@router.message(F.text == "Obunani yondirish")
async def toggle_subscription_status(message: Message):
    user = db.get_user(message.from_user.id)  # { "id": 1, "name": "...", "is_subscribed": 1, ... }
    is_subscribed = user.get("is_subscribed") == 1
    
    db.manage_subscription(is_subscribed=0 if is_subscribed else 1, telegram_id=message.from_user.id)

    await message.answer(text=f"Obuna {'ochirildi ❌' if is_subscribed else 'yondirildi ✅'}", reply_markup=generate_settings_menu(telegram_id=message.from_user.id))

