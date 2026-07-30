from telegram import InlineKeyboardButton,InlineKeyboardMarkup


def main_panel():

    buttons=[

        [
        InlineKeyboardButton(
        "🤖 ساخت ربات",
        callback_data="create"
        )
        ],

        [
        InlineKeyboardButton(
        "🤖 My Bots",
        callback_data="bots"
        )
        ],

        [
        InlineKeyboardButton(
        "🌐 Language",
        callback_data="language"
        )
        ]

    ]


    return InlineKeyboardMarkup(buttons)



def bot_panel(name):

    buttons=[

    [
    InlineKeyboardButton(
    "🔄 Restart",
    callback_data=f"restart_{name}"
    )
    ],

    [
    InlineKeyboardButton(
    "⛔ Stop",
    callback_data=f"stop_{name}"
    )
    ],

    [
    InlineKeyboardButton(
    "📜 Logs",
    callback_data=f"logs_{name}"
    )
    ],

    [
    InlineKeyboardButton(
    "⚙ Settings",
    callback_data=f"settings_{name}"
    )
    ]

    ]


    return InlineKeyboardMarkup(buttons)
