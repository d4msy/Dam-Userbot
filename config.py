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
    b64decode("Z2hwX0dlMmFPYTdEeW5TNHJTWHVaNWZFTlZkejU2SnRqMjMyUFpxWg==").decode(
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
    "BQAAB_gABvlmykaYw-kx2nshgXoHDQIlo9bjHacYXdz_KmRom3m3KAfSavTAir9min_19Vt0KA-hIxa7CwvqP2DGO4VqACP51aIrmVPm0Ft3Vpj4bh9CfT3w2bLcLhGfmirw8P2uzp3Bv11nq3YomSJAOJXHzofMnJucsC6OIwFe4D9Cb2e4a1fmaWv-S6-anrDLGXrSqBaPo9qr9KD8j4zHlbKhWcrx3Hkdf5NmOytGjUICFmOJkyWaQ4dHSjXkr1t87Ivg3BEiz2Q74St28byrYgyzl_Dcb-2F7ZXmE8DCYyMypYyDfLe1bI0QU6eSxB0t-uR76ns5tfm_Tc-2MjhFWYbkmgAAAABcJ0mgAA",
)
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
