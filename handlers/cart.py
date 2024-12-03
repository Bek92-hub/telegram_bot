from aiogram.types import Message
from aiogram import F

from router import router
from loader import db
from keyboards.inline.cart import generate_cart_menu


@router.message(F.text == "🛒 Savatcha")
async def cart(message: Message):
    telegram_id = message.from_user.id
    user = db.get_user(telegram_id=telegram_id)
    user_id = user.get('id')
    orders = db.get_cart_products(user_id=user_id)

    text = "🛒 Sizning savatchangizda\n\n"
    counter = 0
    final_price = 0

    for order in orders:
        counter += 1
        total_price = f"{order.get('total_price'):,.2f}".replace(",", " ")
        final_price += order.get('total_price')
        product = db.get_product(product_id=order.get('product_id'))

        text += f"{counter}) ----------\n"
        text += f"Maxsulot: <b>{product.get('name')}</b>\n"
        text += f"Soni: <b>{order.get('quantity')} ta</b>\n"
        text += f"Umumiy narx: <b>{total_price} so'm</b>\n\n"

    final_price = f"{final_price:,.2f}".replace(",", " ")
    text += f"Savatcha narxi: <b>{final_price} so'm</b>"

    if len(orders) > 0:
        await message.answer(text=text, parse_mode="HTML", reply_markup=generate_cart_menu())
    else:
        await message.answer(text="😐 Savatchangiz bo'sh")
