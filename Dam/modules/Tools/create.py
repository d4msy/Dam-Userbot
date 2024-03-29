# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# Dam-PyroBot

from pyrogram import Client, filters
from pyrogram.types import Message

from Dam.modules.Ubot.help import add_command_help


@Client.on_message(filters.command("create", [".", "-", "^", "!", "?"]) & filters.me)
async def create(client: Client, message: Message):
    if len(message.command) < 3:
        return await message.reply("**Ketik .help misc bila membutuhkan bantuan**")
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    Dam = await message.reply("♻️ `Processing...`")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "gc":  # for supergroup
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id["id"])
        await Dam.edit(
            f"*☑️ **Successfully Create Telegram Group: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )
    elif group_type == "ch":  # for channel
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id["id"])
        await Dam.edit(
            f"**☑️ Successfully Create Telegram Channel: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )


add_command_help(
    "create",
    [
        [".create ch", "Untuk membuat channel telegram dengan userbot"],
        [".create gc", "Untuk membuat group telegram dengan userbot"],
    ],
)
