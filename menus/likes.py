from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import dp, bot, types, ADMIN
from aiogram.dispatcher import FSMContext
from instagpy import InstaGPy
from states import States

from Keyboards.inline import *
from Keyboards.defualt import *

son_likes = {}


@dp.message_handler(text="Likes ❤️")
async def likes(message: types.Message):
    global tg_username
    tg_username = message.from_user.username
    son_likes[message.from_user.id] = 0
    await message.answer("Instagram Usernamingizni kiriting ⬇️")
    await States.likes_username.set()


@dp.message_handler(content_types='text', state=States.likes_username)
async def likeuser(message: types.Message, state: FSMContext):
    username = str(message.text)
    try:
        global txt
        insta = InstaGPy(use_mutiple_account=False, session_ids=None, min_requests=None, max_requests=None)
        txt = insta.get_user_basic_details(username)
        await message.answer_photo(photo=open("images/like.png", "rb"), reply_markup=likes_btn, caption="""
    Tanlang:        
            """)
        await state.finish()
    except:
        await message.answer(f"""
    Bunday Instagram profil mavjud emas <a href="https://www.instagram.com/{username}">{username}</a> 
    """)
        await state.finish()


@dp.callback_query_handler(text="like_plus")
async def likes(call: types.CallbackQuery):
    son_likes[call.message.chat.id] += 1000
    update_like_btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("-", callback_data='like_minus'),
                InlineKeyboardButton(son_likes[call.message.chat.id], callback_data='son'),
                InlineKeyboardButton("+", callback_data='like_plus')
            ],
            [
                InlineKeyboardButton("Tasdiqlash ✅", callback_data='like_tasdiqlash'),
            ]
        ]
    )
    await call.message.edit_media(
        media=types.InputMediaPhoto(open("images/like.png", "rb"), caption="Tanlang:"),
        reply_markup=update_like_btn
    )


@dp.callback_query_handler(text="like_minus")
async def likes(call: types.CallbackQuery):
    son_likes[call.message.chat.id] -= 1000
    update_like_btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("-", callback_data='like_minus'),
                InlineKeyboardButton(son_likes[call.message.chat.id], callback_data='son'),
                InlineKeyboardButton("+", callback_data='like_plus')
            ],
            [
                InlineKeyboardButton("Tasdiqlash ✅", callback_data='like_tasdiqlash'),
            ]
        ]
    )
    await call.message.edit_media(
        media=types.InputMediaPhoto(open("images/like.png", "rb"), caption="Tanlang:"),
        reply_markup=update_like_btn
    )



@dp.callback_query_handler(text="like_tasdiqlash")
async def likestasdiq(call: types.CallbackQuery):
    user_id = call.message.chat.id
    await call.message.reply(f"""
<b>Xizmat turi</b>: Likes ❤️

<b>Username</b>: {txt['username']}

<b>Telegram Username</b>: {tg_username}

<b>Soni</b>: {son_likes[user_id]} 

<b>Narxi</b>: {son_likes[user_id] * 5} so'm 💰

<b>To'lov karta raqami 💳</b>: <code>9860160103219319</code>
    """, reply_markup=send_check_button_likes)


# @dp.message_handler(text="likes_check")
# async def checckk(call: types.CallbackQuery):