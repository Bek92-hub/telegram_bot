from aiogram.types import CallbackQuery
from aiogram import F

from router import router
from keyboards.inline.categories import generate_categories_menu


@router.callback_query(F.data == "back-to-categories")
async def back_to_categories(call: CallbackQuery):
    await call.message.edit_reply_markup(text="Harakatni tanlang", reply_markup=generate_categories_menu())