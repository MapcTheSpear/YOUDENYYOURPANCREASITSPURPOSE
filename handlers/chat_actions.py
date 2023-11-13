import datetime
import sqlite3

from aiogram import types, Dispatcher
from config import bot, DESTINATION
from database.sql_commands import Database
from keyboards.inline_buttons import start_keyboard
from const import START_MENU
from profanity_check import predict, predict_prob


async def chat_messages(message: types.Message):
    db = Database()
    print(message)
    if message.chat.id == -1002068432758:
        ban_word_predict_prob = predict_prob([message.text])
        if ban_word_predict_prob > 0.1:
            await message.delete()
            user = db.sql_select_ban_user(
                telegram_id=message.from_user.id
            )
            await bot.send_message(
                chat_id=message.chat.id,
                text=f'User: {message.from_user.id} {message.from_user.first_name}\n'
                     f'Shut yo mouth\n'
                     f'Mf, you got warned:{user["count"]} times, on third ull be banned for good'
            )
            print(user)
            count = user['count']
            if not user:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text =f'{message.from_user.first_name} This mf got banned!'
                )
                db.sql_insert_ban_users(
                    telegram_id=message.from_user.id
                )
            elif count >= 3:
                await bot.ban_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.from_user.id,
                    until_date=datetime.datetime.now() + datetime.timedelta(seconds=25)
                )
            elif user:
                db.sql_update_ban_user_count(
                    telegram_id=message.from_user.id
                )
            # db.sql_insert_ban_users(
            #     telegram_id=message.from_user.id
            # )
    else:
        await message.reply(
            text='Dunno wut u be talking dude.'
        )


def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_messages)
