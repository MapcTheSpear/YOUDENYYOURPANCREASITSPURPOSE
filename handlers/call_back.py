import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from keyboards.inline_buttons import questionnaire_keyboard


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


def register_callback_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(bloods_call,
                                       lambda call: call.data == "bloods")
    dp.register_callback_query_handler(crips_call,
                                       lambda call: call.data == "crips")