from aiogram.types import CallbackQuery
from aiogram import F

from router import router
from keyboards.inline.product import generate_product_menu

# "product-action:decrement:1:1"
# "product-action:increment".split(":") => ["product-action", "increment"]
@router.callback_query(F.data.split(":")[0] == "product-action")
async def product_action(call: CallbackQuery):
    action = call.data.split(":")[1]
    quantity = int(call.data.split(":")[2])
    category_id = int(call.data.split(":")[3])
    product_id = int(call.data.split(":")[4])

    if action == "increment":
        quantity += 1

    elif action == "decrement":
        if quantity - 1 >= 1:
            quantity -= 1

    await call.message.edit_reply_markup(
        reply_markup=generate_product_menu(category_id=category_id, product_id=product_id, quantity=quantity)
    )
