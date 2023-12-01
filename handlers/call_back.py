import sqlite3

from aiogram import types, Dispatcher
from config import bot, ADMIN_ID
from database.sql_commands import Database
from keyboards.inline_buttons import questionnaire_keyboard
from scraping.spirit_scraper import SpiritScraper


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Bloods or Crips, huh?',
        reply_markup=await questionnaire_keyboard()
    )


async def bloods_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Shi, homie, you be Bloods for real? '
    )


async def crips_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Ay, you good, you good, Crips 4 life'
    )


async def admin_call(call: types.CallbackQuery):
    if call.from_user.id == int(ADMIN_ID):
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Sup, bro, aint forgettin u"
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Who tf are u?"
        )

async def anima_call(call : types.CallbackQuery):
    scraper = SpiritScraper()
    data = scraper.parse_data()
    for url in data[:5]:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f'{url}'
        )

def register_callback_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(bloods_call,
                                       lambda call: call.data == "bloods")
    dp.register_callback_query_handler(crips_call,
                                       lambda call: call.data == "crips")
    dp.register_message_handler(admin_call,
                                       lambda word: "dorei" in word.text)
    dp.register_callback_query_handler(anima_call,
                                       lambda  call: call.data == 'anime')
