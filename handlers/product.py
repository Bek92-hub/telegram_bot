from aiogram.types import CallbackQuery

from router import router
from loader import db
from keyboards.inline.product import generate_product_menu


@router.callback_query(lambda call: "product" == call.data.split(":")[0])
async def product(call: CallbackQuery):
    product_id = int(call.data.split(":")[-1])
    product = db.get_product(product_id)
    
    await call.message.delete()
    await call.message.answer_photo(
        photo=product.get("photo"),
        caption=f"Maxsulot: <b>{product.get('name')}</b>\n\nMaxsulot haqida: <b>{product.get('description')}</b>\n\nNarxi: <b>{product.get('price')} so'm</b>",
        parse_mode="HTML",
        has_spoiler=True,
        reply_markup=generate_product_menu(category_id=product.get("category_id"), product_id=product_id)
    )
