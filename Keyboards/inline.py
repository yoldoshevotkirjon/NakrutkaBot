from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


follower_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("-", callback_data='follower_minus'),
            InlineKeyboardButton("0", callback_data='son'),
            InlineKeyboardButton("+", callback_data='follower_plus')
        ],
        [
            InlineKeyboardButton("Tasdiqlash ✅", callback_data='follower_tasdiqlash'),
        ]
    ]
)

send_check_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Chekni Yuborish",callback_data="check"),
        ]
    ]
)


check_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Ha ✅", callback_data='check_true'),
            InlineKeyboardButton("Yoq ❌", callback_data='check_false'),
        ]
    ]
)


likes_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("-", callback_data='like_minus'),
            InlineKeyboardButton("0", callback_data='son'),
            InlineKeyboardButton("+", callback_data='like_plus')
        ],
        [
            InlineKeyboardButton("Tasdiqlash ✅", callback_data='like_tasdiqlash'),
        ]
    ]
)


send_check_button_likes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Chekni Yuborish",callback_data="likes_check"),
        ]
    ]
)
