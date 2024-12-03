from aiogram.types import CallbackQuery

from router import router
from keyboards.inline.products import generate_products_menu


@router.callback_query(lambda call: "category" in call.data)
async def products(call: CallbackQuery):
    category_id = int(call.data.split(":")[-1])  # "category:1".split(":") => ["category", "1"]

    await call.message.edit_reply_markup(reply_markup=generate_products_menu(category_id))
