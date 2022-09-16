# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# Dam-PyroBot

import asyncio
import os
import time
from platform import python_version

from pyrogram import Client
from pyrogram import __version__ as versipyro
from pyrogram import filters
from pyrogram.types import Message
from telegraph import exceptions, upload_file

from config import BOT_VER, GROUP
from Dam import CMD_HELP, StartTime
from Dam.helpers.basic import edit_or_reply
from Dam.helpers.PyroHelpers import ReplyCheck
from Dam.helpers.SQL.globals import gvarstatus
from Dam.helpers.tools import convert_to_image
from Dam.utils import get_readable_time
from Dam.utils.misc import restart

from .help import add_command_help

modules = CMD_HELP
alive_logo = (
    gvarstatus("ALIVE_LOGO") or "https://telegra.ph/file/3ed0efba4cad047af8966.jpg"
)
emoji = gvarstatus("ALIVE_EMOJI") or "•"
alive_text = gvarstatus("ALIVE_TEKS_CUSTOM") or "👋 Hey, I am Alive!"


@Client.on_message(
    filters.command(["alive", "dam"], [".", "-", "^", "!", "?"]) & filters.me
)
async def alive(client: Client, message: Message):
    xx = await edit_or_reply(message, "🔥")
    await asyncio.sleep(2)
    send = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    uptime = await get_readable_time((time.time() - StartTime))
    man = (
        f"**[PyroDam-Userbot](https://github.com/damsyx/Dam-Ubot) is Up And Running!**\n\n"
        f"<b>{alive_text}</b>\n\n"
        f"{emoji} <b>**Owner** -≽</b> {client.me.mention} \n"
        f"{emoji} <b>**Modules** -≽</b> <code>{len(modules)} Modules</code> \n"
        f"{emoji} <b>**Dam Version** -≽</b> <code>{BOT_VER}</code> \n"
        f"{emoji} <b>**Python Version** -≽</b> <code>{python_version()}</code> \n"
        f"{emoji} <b>**Pyrogram Version** -≽</b> <code>{versipyro}</code> \n"
        f"{emoji} <b>**Bot Uptime** -≽</b> <code>{uptime}</code> \n"
        f"{emoji} <b>**Group Support** -≽</b> [Dam-Support](https://t.me/{GROUP})"
    )
    try:
        await asyncio.gather(
            xx.delete(),
            send(
                message.chat.id,
                alive_logo,
                caption=man,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(man, disable_web_page_preview=True)


@Client.on_message(
    filters.command("setalivelogo", [".", "-", "^", "!", "?"]) & filters.me
)
async def setalivelogo(client: Client, message: Message):
    try:
        import Dam.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    Man = await edit_or_reply(message, "`Processing...`")
    link = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await Man.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        link = f"https://telegra.ph/{media_url[0]}"
        os.remove(m_d)
    sql.addgvar("ALIVE_LOGO", link)
    await Man.edit(
        f"**Berhasil Mengcustom ALIVE LOGO Menjadi {link}**",
        disable_web_page_preview=True,
    )
    restart()


@Client.on_message(
    filters.command("setalivetext", [".", "-", "^", "!", "?"]) & filters.me
)
async def setalivetext(client: Client, message: Message):
    try:
        import Dam.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    Man = await edit_or_reply(message, "`Processing...`")
    if not text:
        return await edit_or_reply(
            message, "**Berikan Sebuah Text atau Reply ke text**"
        )
    sql.addgvar("ALIVE_TEKS_CUSTOM", text)
    await Man.edit(f"**Berhasil Mengcustom ALIVE TEXT Menjadi** `{text}`")
    restart()


@Client.on_message(filters.command("setemoji", [".", "-", "^", "!", "?"]) & filters.me)
async def setemoji(client: Client, message: Message):
    try:
        import Dam.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    emoji = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    Man = await edit_or_reply(message, "`Processing...`")
    if not emoji:
        return await edit_or_reply(message, "**Berikan Sebuah Emoji**")
    sql.addgvar("ALIVE_EMOJI", emoji)
    await Man.edit(f"**Berhasil Mengcustom EMOJI ALIVE Menjadi** {emoji}")
    restart()


add_command_help(
    "alive",
    [
        [
            ".alive or .dam",
            "Untuk memeriksa userbot anda berfungsi atau tidak",
        ],
        [
            "setalivelogo <link telegraph atau reply ke foto/video/gif>",
            "Untuk mengcustom alive logo userbot anda",
        ],
        [
            "setalivetext <text>",
            "Untuk mengcustom alive text userbot anda",
        ],
        [
            "setemoji <emoji>",
            "Untuk mengcustom emoji alive userbot anda",
        ],
    ],
)
