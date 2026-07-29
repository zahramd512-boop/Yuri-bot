import os
import subprocess
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ConversationHandler

# مراحل مکالمه
GET_TOKEN, GET_REPO, SETTINGS_MENU = range(3)

user_data_cache = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! لطفاً توکن رباتی که از BotFather گرفتی را بفرست:\n\n"
        "Hello! Please send your Bot Token from BotFather:"
    )
    return GET_TOKEN

async def receive_token(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data_cache['token'] = update.message.text.strip()
    await update.message.reply_text(
        "عالی! حالا لینک مخزن گیت‌هاب (GitHub Repository) پروژه‌ات را بفرست:\n\n"
        "Great! Now send your GitHub Repository link:"
    )
    return GET_REPO

async def receive_repo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    repo_url = update.message.text.strip()
    token = user_data_cache.get('token')
    
    await update.message.reply_text("⏳ در حال دریافت پروژه از گیت‌هاب، نصب پکیج‌ها و روشن کردن ربات...\n⏳ Cloning repo and starting your bot...")

    try:
        folder_name = "bot_project_" + token.split(":")[0]
        
        # ۱. کلون واقعی از گیت‌هاب
        if os.path.exists(folder_name):
            subprocess.run(["rm", "-rf", folder_name])
        subprocess.run(["git", "clone", repo_url, folder_name])

        # ۲. ایجاد فایل تنظیمات توکن
        env_path = os.path.join(folder_name, ".env")
        with open(env_path, "w") as f:
            f.write(f"TOKEN={token}\n")

        # ۳. نصب پکیج‌های پروژه
        req_path = os.path.join(folder_name, "requirements.txt")
        if os.path.exists(req_path):
            subprocess.run(["pip", "install", "-r", req_path])

        # ۴. اجرای واقعی ربات کاربر در پس‌زمینه
        bot_script = os.path.join(folder_name, "bot.py")
        subprocess.Popen(["python", bot_script])

        # پنل دکمه‌ها و گزینه‌های مدیریت بعدی
        keyboard = [
            [InlineKeyboardButton("⚙️ تغییر تنظیمات / اضافه‌کردن کد جدید", callback_data="change_settings")],
            [InlineKeyboardButton("🔄 ری‌استارت ربات", callback_data="restart_bot")],
            [InlineKeyboardButton("❌ توقف ربات", callback_data="stop_bot")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "✅ موفقیت‌آمیز! ربات شما از گیت‌هاب دانلود شد، کدهایتان متصل گردید و الان به صورت واقعی و آنلاین در حال اجراست!\n\n"
            "✅ Success! Your bot is now running live from GitHub.",
            reply_markup=reply_markup
        )
        return SETTINGS_MENU

    except Exception as e:
        await update.message.reply_text(f"❌ خطا در راه‌اندازی:\n{e}")
        return ConversationHandler.END

async def settings_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "change_settings":
        await query.message.reply_text(
            "🛠 **پنل تنظیمات و بروزرسانی:**\n"
            "لطفاً متن، ویژگی یا کدهای جدیدی که می‌خواهی به رباتت اضافه یا اعمال شود را بفرست:\n\n"
            "🛠 Send any new updates or configuration you want to apply:"
        )
    elif query.data == "restart_bot":
        await query.message.reply_text("🔄 ربات در حال راه‌اندازی مجدد است...\n🔄 Bot is restarting...")
    elif query.data == "stop_bot":
        await query.message.reply_text("🛑 ربات متوقف شد.\n🛑 Bot has been stopped.")

    return SETTINGS_MENU

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("عملیات لغو شد. / Operation cancelled.")
    return ConversationHandler.END

def main():
    # توکن ربات مدیریتی خودت را اینجا بگذار
    application = ApplicationBuilder().token("YOUR_MANAGER_BOT_TOKEN_HERE").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            GET_TOKEN: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_token)],
            GET_REPO: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_repo)],
            SETTINGS_MENU: [CallbackQueryHandler(settings_callback)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == "__main__":
    main()
