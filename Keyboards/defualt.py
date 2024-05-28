from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


phone_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("☎️ Telefon Nomerni Yuborish",request_contact=True)
        ]
    ],
    resize_keyboard=True
)


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Followers 👤"),
            KeyboardButton(text="Likes ❤️")
        ],
        [
            KeyboardButton(text="Views 👁️"),
            KeyboardButton(text="Comments 💬")
        ]
    ],
    resize_keyboard=True,
)


