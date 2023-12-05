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
    my_profile_button = InlineKeyboardButton(
        "My profile, nigga",
        callback_data="my_profile"
    )
    random_profiles_button = InlineKeyboardButton(
        "Show me other niggas",
        callback_data="random_profiles"
    )
    reference_menu_button = InlineKeyboardButton(
        "Reference Menu 🪲",
        callback_data="reference_menu"
    )
    news_button = InlineKeyboardButton(
        "Latest News",
        callback_data="news"
    )
    mods_button = InlineKeyboardButton(
        "Minecraft Mods",
        callback_data="mods"
    )
    async_mods_button = InlineKeyboardButton(
        "Another Mod Pages",
        callback_data="mod_pages"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(random_profiles_button)
    markup.add(reference_menu_button)
    markup.add(news_button)
    markup.add(mods_button)
    markup.add(async_mods_button)
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

async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Like yo",
        callback_data=f"liked_profile {owner_tg_id}"
    )
    dislike_button = InlineKeyboardButton(
        "Eww wtf",
        callback_data="random_profiles"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    edit_button = InlineKeyboardButton(
        "Edit yo",
        callback_data=f"update_profile"
    )
    delete_button = InlineKeyboardButton(
        "Delete this",
        callback_data="delete"
    )
    back_button = InlineKeyboardButton(
        "Get back",
        callback_data="back"
    )
    markup.add(edit_button)
    markup.add(delete_button)
    markup.add(back_button)
    return markup


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    reference_button = InlineKeyboardButton(
        "Reference Link 🔗",
        callback_data="reference_link"
    )
    referal_list = InlineKeyboardButton(
        "List of Referals",
        callback_data="list_of_referals"
    )
    markup.add(reference_button)
    markup.add(referal_list)
    return markup
