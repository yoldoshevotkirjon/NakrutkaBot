from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import dp, bot, types, ADMIN
from aiogram.dispatcher import FSMContext
from instagpy import InstaGPy
from states import States

from Keyboards.inline import *
from Keyboards.defualt import *

son_follow = {}


@dp.message_handler(text='Followers 👤')
async def follow(message: types.Message):
    global tg_username
    son_follow[message.from_user.id] = 0
    tg_username = message.from_user.username
    await message.answer("Instagram Usernamingizni kiriting ⬇️")
    await States.follow_username.set()


@dp.message_handler(content_types='text', state=States.follow_username)
async def follow(message: types.Message, state: FSMContext):
    username = str(message.text)
    try:
        global txt
        insta = InstaGPy(use_mutiple_account=False, session_ids=None, min_requests=None, max_requests=None)
        txt = insta.get_user_basic_details(username)
        await message.answer_photo(photo=open("images/follower.png", "rb"), reply_markup=follower_btn, caption="""
Tanlang:        
        """)
        await state.finish()
    except:
        await message.answer(f"""
Bunday Instagram profil mavjud emas <a href="https://www.instagram.com/{username}">{username}</a>
""")
        await state.finish()


@dp.callback_query_handler(text='follower_plus')
async def follow(call: types.CallbackQuery):
    user_id = call.message.chat.id
    son_follow[user_id] += 1000

    update_follower_btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("-", callback_data='follower_minus'),
                InlineKeyboardButton(str(son_follow[user_id]), callback_data='son'),
                InlineKeyboardButton("+", callback_data='follower_plus')
            ],
            [
                InlineKeyboardButton("Tasdiqlash ✅", callback_data='follower_tasdiqlash'),
            ]
        ]
    )

    await call.message.edit_media(
        media=types.InputMediaPhoto(open("images/follower.png", "rb"), caption="Tanlang:"),
        reply_markup=update_follower_btn
    )


@dp.callback_query_handler(text='follower_minus')
async def follow(call: types.CallbackQuery):
    user_id = call.message.chat.id
    son_follow[user_id] -= 1000

    update_follower_btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("-", callback_data='follower_minus'),
                InlineKeyboardButton(str(son_follow[user_id]), callback_data='son'),
                InlineKeyboardButton("+", callback_data='follower_plus')
            ],
            [
                InlineKeyboardButton("Tasdiqlash ✅", callback_data='follower_tasdiqlash'),
            ]
        ]
    )

    await call.message.edit_media(
        media=types.InputMediaPhoto(open("images/follower.png", "rb"), caption="Tanlang:"),
        reply_markup=update_follower_btn
    )


@dp.callback_query_handler(text='follower_tasdiqlash')
async def tasdiqfollow(call: types.CallbackQuery):
    user_id = call.message.chat.id
    await call.message.reply(f"""
<b>Xizmat Turi</b>: Followers 👤

<b>Username</b>: <a href="https://www.instagram.com/{txt['username']}">{txt['username']}</a> 

<b>Telegram Username</b>: <a href="https://www.instagram.com/{tg_username}">{tg_username}</a>

<b>Soni</b>: {son_follow[user_id]}

<b>Narxi</b>:{son_follow[user_id] * 5} so'm 💰

<b>To'lov karta raqami 💳</b>: <code>9860160103219319</code>
    """, reply_markup=send_check_button)


@dp.callback_query_handler(text='check')
async def checkk(call: types.CallbackQuery):
    await call.message.answer("Chekni yuboring")
    await States.send_check.set()


@dp.message_handler(content_types='photo', state=States.send_check)
async def sendd_check(message: types.Message, state: FSMContext):
    global buyurtmachi_user_id
    buyurtmachi_user_id = message.from_user.id
    file_id = message.photo[-1].file_id
    await bot.send_photo(ADMIN, photo=file_id, caption=f"""
Chekni Togriligni Tasdiqlang    
    """, reply_markup=check_button)
    await message.answer("Chekingiz admin tomonidan 24 soat ichida tasdiqlanadi")
    await state.finish()


@dp.callback_query_handler(text='check_true')
async def checktrue(call: types.CallbackQuery):
    await bot.send_message(buyurtmachi_user_id, """
Chekingiz tog'ri ekanligi tasdiqlandi    

Sizning buyurtmangiz 24 soat ichida amalga oshiriladi
    """)
    await bot.send_message(ADMIN, "Check muvofaqiyatli tekshirdingiz")
