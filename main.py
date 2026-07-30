from telegram import Update
from telegram.ext import *

from config import MANAGER_TOKEN

from panel import main_panel,bot_panel

from language import text,change_language

from bot_manager import create_bot

from database import add_bot,get_bots

from updater import update_code



users={}



async def start(update,context):

    user=update.effective_user.id


    await update.message.reply_text(
        text(user,"start"),
        reply_markup=main_panel()
    )



async def buttons(update,context):

    query=update.callback_query

    await query.answer()


    data=query.data



    if data=="language":

        change_language(
            query.from_user.id
        )


        await query.message.reply_text(
            "🌐 Language Changed"
        )



    elif data=="bots":

        bots=get_bots()


        if not bots:

            await query.message.reply_text(
            "No Bots"
            )

            return


        for bot in bots:

            await query.message.reply_text(
                bot["name"],
                reply_markup=
                bot_panel(bot["name"])
            )



    elif data=="create":

        users[
        query.from_user.id
        ]="waiting_repo"


        await query.message.reply_text(
        "GitHub Link را بفرست"
        )



async def messages(update,context):

    user=update.effective_user.id


    if users.get(user)=="waiting_repo":


        repo=update.message.text


        name=f"bot_{user}"


        create_bot(
            name,
            repo
        )


        add_bot(
        {
        "name":name,
        "status":"Running"
        }
        )


        users[user]=None


        await update.message.reply_text(
        "✅ Bot Created"
        )



async def update_command(update,context):

    await update.message.reply_text(
    "کد جدید را ارسال کن"
    )



app=Application.builder().token(
MANAGER_TOKEN
).build()



app.add_handler(
CommandHandler(
"start",
start
)
)


app.add_handler(
CommandHandler(
"update",
update_command
)
)


app.add_handler(
CallbackQueryHandler(
buttons
)
)


app.add_handler(
MessageHandler(
filters.TEXT,
messages
)
)



app.run_polling()
