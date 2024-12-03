from aiogram.types import CallbackQuery, LabeledPrice, ShippingQuery, ShippingOption, PreCheckoutQuery, Message
from aiogram import F

from router import router
from config import PAYMENT_TOKEN


@router.shipping_query()
async def return_shipping_option(shipping_query: ShippingQuery):
    shipping_options = [
        ShippingOption(id='standart-delivery', title="Stanadart yetkazib berish",
                       prices=[LabeledPrice(label="Oddiy yetkaizb berish", amount=15000 * 100)]),
        ShippingOption(id='fast-delivery', title="Zudlik bilan yetkazib berish",
                       prices=[LabeledPrice(label="Tez yetkaizb berish", amount=50000 * 100)]),
    ]
    await shipping_query.answer(
        ok=True,
        shipping_options=shipping_options
    )


@router.callback_query(F.data == "pay")
async def pay(call: CallbackQuery):
    await call.message.answer_invoice(
        title="Sizning savatchangizni narxi",
        description="Umumiy narx: 50 000 so'm",
        payload="{'id': 1, 'cart_id': 2}",
        provider_token=PAYMENT_TOKEN,
        prices=[
            LabeledPrice(label="Lavash (standart)", amount=23000 * 100),
            LabeledPrice(label="Coca-cola 0.5", amount=7000 * 100)
        ],
        photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQz4EwRe31j7RxW01OfOPkZ5PD3a8cDvff4Hw&s",
        currency="uzs",
        max_tip_amount=5000 * 100,
        suggested_tip_amounts=[1000 * 100,
                               2000 * 100,
                               3000 * 100,
                               4000 * 100],
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=True,
        is_flexible=True,
    )


@router.pre_checkout_query(lambda call: True)
async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True, error_message="Maxsulot qolmagan")


@router.message()
async def finish(message: Message):
    if message.successful_payment:
        await message.answer(text="To'lovingiz qabul qilindi")
