# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("API_HASH", "e2432085a412bbc89e1d5bbcd72a7f0d")
API_ID = int(getenv("API_ID", "9317779"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001599474353, -1001473548283, -1001687155877]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "0.2.0@main"
BRANCH = "main"
CHANNEL = getenv("CHANNEL", "d4mch")
DB_URL = getenv(
    "DATABASE_URL",
    "postgres://mvedakyh:dIjsnpYu5cWqD_4Bkyjqi2r-MZTf4FQh@tyke.db.elephantsql.com/mvedakyh",
)
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwXzVJa1U4V2dMeHh6VUR5NGVIRzZRb042QzJ4dndGUjRhSzM0dw==").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "HimikoSupportChat")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "False"))

STRING_SESSION1 = getenv(
    "STRING_SESSION1",
    "BQE2rfMApO37BeeLudbtb8BvSAwFUzXEWoO4-NtRlxBSoLYd7886sRQ_Vod_TDCnlK4EcZXomr23l__EYa0ijYZkEKg66JzFdUxMYKkTDIFp0zwLfIG31miqkXNRizW0J6MyAJQbGQdD-CJdhRlv8-j6QO7NoZDh7YmyYrgilvoOxiGSRtru8DmCs1ds_kXv8FS5hhxxQl17KLz24dsLSXyl0HN8D3yFIbjGbNc0_1pmeZgPGAj_ML3-7ZZqJQg8sRDxkOkxVD121HF_VEpaBbMiQ9U9s4sBOMHbiWWiq0ESNCrVzX2H2EEXQPMGfT_JoAcnBW0Fw5RrTrwiewBlgGZtf59RXwAAAABm26eIAA",
)
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
