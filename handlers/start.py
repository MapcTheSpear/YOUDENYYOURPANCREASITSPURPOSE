import sqlite3

from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link
from config import bot, DESTINATION
from database.sql_commands import Database
from keyboards.inline_buttons import start_keyboard
from const import START_MENU


async def start_button(message: types.Message):
    print(message)
    db = Database()
    print(message.get_full_command())
    command = message.get_full_command()
    if command[1] != "":
        link = await _create_link(link_type="start", payload=command[1])
        user = db.sql_select_user_by_link(
            link=link
        )
        print(user)

        if user['tg_id'] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text="Нельзя переходить по своей ссылке"
            )
            return
        else:
            try:
                db.sql_update_balance(
                    tg_id=user['tg_id']
                )
                db.sql_insert_referral(
                    owner=user['tg_id'],
                    referral=message.from_user.id
                )
            except sqlite3.IntegrityError:
                pass
    try:
        db.sql_insert_users(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
    except sqlite3.IntegrityError:
        pass

    # with open(DESTINATION + "cj.jpg", 'rb') as photo:
    #     await bot.send_photo(
    #         chat_id=message.from_user.id,
    #         photo=photo,
    #         caption=START_MENU.format(
    #             user=message.from_user.first_name
    #         ),
    #         reply_markup=await start_keyboard()
    #     )

    with open (DESTINATION + "cjgif.gif", "rb") as animation:
        await bot.send_animation(
            chat_id=message.from_user.id,
            animation=animation,
            caption=START_MENU.format(
                user=message.from_user.first_name
            ),
            reply_markup=await start_keyboard()
        )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])


