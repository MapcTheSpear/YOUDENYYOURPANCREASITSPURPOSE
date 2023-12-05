import sqlite3

from aiogram import types, Dispatcher
from config import bot, ADMIN_ID
from database.sql_commands import Database
from keyboards.inline_buttons import questionnaire_keyboard
# from scraping.news_scraper import NewsScraper
# from scraping.minecraft_mods import ModsScrapper
# from scraping.async_mods import AsyncModsScrapper


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


# async def scraper_call(call: types.CallbackQuery):
#     scraper = NewsScraper()
#     data = scraper.parse_data()
#     for url in data[:4]:
#         await bot.send_message(
#             chat_id=call.from_user.id,
#             text=f"{scraper.PLUS_URL + url}"
#         )


# async def mods_scraper(call: types.CallbackQuery):
#     scraper = ModsScrapper()
#     data = scraper.parse_data()
#     for url in data[:4]:
#         await bot.send_message(
#             chat_id=call.from_user.id,
#             text=url
#         )


# async def async_mods_scraper(call:types.CallbackQuery):
#     scraper = AsyncModsScrapper
#     data = scraper.parse_pages
#     for url in data[:5]:
#         await bot.send_message(
#             chat_id=call.from_user.id,
#             text=url
#         )

def register_callback_handlers(dp:Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(bloods_call,
                                       lambda call: call.data == "bloods")
    dp.register_callback_query_handler(crips_call,
                                       lambda call: call.data == "crips")
    dp.register_message_handler(admin_call,
                                       lambda word: "dorei" in word.text)
    # dp.register_callback_query_handler(scraper_call,
    #                                    lambda call: call.data == 'news')
    # dp.register_callback_query_handler(mods_scraper,
    #                                    lambda call: call.data == 'mods')
    # dp.register_callback_query_handler(async_mods_scraper,
    #                                    lambda call: call.data == 'mod_pages')
