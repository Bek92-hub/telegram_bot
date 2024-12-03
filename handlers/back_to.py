from aiogram.types import CallbackQuery

from router import router
from loader import db
from keyboards.inline.products import generate_products_menu


@router.callback_query(lambda call: "back-to" in call.data.split(":")[0])
async def back_to_category(call: CallbackQuery):
    category_id = int(call.data.split(":")[-1])

    await call.message.delete()
    await call.message.answer(text="Harakatni tanlang", reply_markup=generate_products_menu(category_id))
