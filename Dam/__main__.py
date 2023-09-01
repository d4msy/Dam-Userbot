# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# Dam-PyroBot

from pyrogram import idle
from uvloop import install

from config import BOT_VER
from Dam import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from Dam.helpers.misc import create_botlog, git, heroku

MSG_ON = """
┌| **Dam-Ubot Berhasil Di Aktifkan.** |┘
━━
◈ **🤖 Userbot Version -** `{}`
◈ **Ketik** `.alive` **Untuk Mengecheck Bot.**
━━
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("SharingUserbot")
            await bot.join_chat("d4mch")
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER))
            except BaseException:
                pass
            LOGGER("Dam").info(f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]")
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("Dam").info(f"Dam-Ubot v{BOT_VER} ⚙️[⚡ Activated ⚡]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Dam").info("Starting Dam-Ubot")
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
