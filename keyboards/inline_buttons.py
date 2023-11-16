from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Ayo, bro, i have a question real quick",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Register here, NOW",
        callback_data="registration"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    return markup


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    bluds_button = InlineKeyboardButton(
        "Bloods",
        callback_data="bloods"
    )
    crips_button = InlineKeyboardButton(
        "Crips",
        callback_data="crips"
    )
    markup.add(bluds_button)
    markup.add(crips_button)
    return markup
