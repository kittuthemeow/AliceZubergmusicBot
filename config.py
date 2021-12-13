import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Bot")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "DeepakJack007")
ALIVE_NAME = getenv("ALIVE_NAME", "Alice Zuberg")
BOT_USERNAME = getenv("BOT_USERNAME", "shukurenaivideobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Shukurenai")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "shukurenairobot007")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "shukurenai007")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/8bcec978a5de69283bdb5.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/DeepakJack007")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/8caf5fef14a7405e452d6.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/a998702b52548cbcc4914.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/538e66d0d58f0e00b26e6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/8abf152a3336f022c0c11.png") 
