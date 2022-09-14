# Cilik-PyroBot

import asyncio

from pyrogram import Client, enums, filters
from pyrogram.errors import RPCError
from pyrogram.types import *

from Cilik.modules.Ubot.help import add_command_help


@Client.on_message(filters.command("nulis", [".", "-", "^", "!", "?"]) & filters.me)
async def nulis(client: Client, message: Message):
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
    if not text:
        return await message.reply("**Berikan Text atau Reply**")
    Cilik = await message.reply("`✍️ Writing...`")
    bot = "awakmalas_bot"
    chat = message.chat.id
    if text:
        try:
            await client.send_message(bot, "/start")
            await asyncio.sleep(0.5)
            await client.send_message(bot, "Font 1")
            await asyncio.sleep(0.5)
            await client.send_message(bot, f"/malas1 {text}")
            await asyncio.sleep(0.5)
            await Cilik.edit("📤 `Uploaded...`")
            await asyncio.sleep(5)
        except RPCError:
            return await Cilik.edit(
                "`Silahkan buka blockir @awakmalas_bot lalu coba lagi`"
            )
    async for kontol in client.search_messages(
        bot, filter=enums.MessagesFilter.PHOTO, limit=1
    ):
        await client.send_photo(
            chat, photo=kontol.photo.file_id, caption=f"📌 **Writing by Cilik-Ubot**"
        )
        await Cilik.delete()
        await kontol.delete()


add_command_help(
    "nulis",
    [
        [
            f".nulis <text> or reply to text",
            "untuk anda yang mager nulis",
        ]
    ],
)
