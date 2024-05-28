from aiogram import executor, types, Dispatcher, Bot
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from Keyboards.defualt import phone_button, menu
from states import States

logging.basicConfig(level=logging.INFO)
token = "7241315241:AAEmhgcK3lqXvu7t7E1eVQKduxZsrTo9xt4"
bot = Bot(token=token, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())

ADMIN = 6457971132


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("<b>I N S T A G R A M </b> botiga xush kelibsiz")
    await message.answer("""
Avval telefon raqamingizni yuboring,
yoki <b>+998XX XXXXXXX</b> ko'rinishida yozing.       
    """, reply_markup=phone_button)
    await States.phone_number.set()


@dp.message_handler(content_types=['contact', 'text'], state=States.phone_number)
async def phone(message: types.Message, state: FSMContext):
    if message.contact:
        await bot.send_message(ADMIN, f"Mijoz telefon raqami : +{message.contact.phone_number}")
        await message.answer(f"""
Bizning qiziqarli Instagram Nakrutka botimizga xush kelibsiz🔥

Ozingizga kerak bo'lgan xizmatimizni tanlang ⬇️
            """, reply_markup=menu)
        await state.finish()
    elif message.text.startswith("+998"):
        await bot.send_message(ADMIN, f"Mijoz telefon raqami : {message.text}")
        await message.answer(f"""
Bizning qiziqarli Instagram Nakrutka botimizga xush kelibsiz🔥

Ozingizga kerak bo'lgan xizmatimizni tanlang ⬇️        
""", reply_markup=menu)
        await state.finish()
    else:
        await message.answer("Noto'g'ri formatdagi telefon raqamini yubordingiz. Iltimos, qaytadan kiriting.", )


if __name__ == '__main__':
    from menus.follow import dp, bot
    from menus.likes import dp, bot
    executor.start_polling(dp, skip_updates=True)
