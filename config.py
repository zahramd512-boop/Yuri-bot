import os
from dotenv import load_dotenv

load_dotenv()

MANAGER_TOKEN = os.getenv("MANAGER_TOKEN")

ADMIN_ID = int(os.getenv("ADMIN_ID",0))

BOT_FOLDER = "bots"

DATABASE = "database.json"
