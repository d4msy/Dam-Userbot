import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from Dam.helpers.PyroHelpers import ReplyCheck
from Dam.modules.Ubot.help import add_command_help
from Dam.utils.misc import extract_user

flood = {}
profile_photo = "ProjectMan/modules/cache/pfp.jpg"


@Client.on_message(filters.command(["block"], [".", "-", "^", "!", "?"]) & filters.me)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    Man = await message.reply("♻️ `Processing...`")
    if not user_id:
        return await message.edit(
            "Provide User ID/Username or reply to user messages to blocking."
        )
    if user_id == client.me.id:
        return await Man.edit("anda stress harap segera minum obat.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Successfully Blocking** {umention}")


@Client.on_message(filters.command(["unblock"], [".", "-", "^", "!", "?"]) & filters.me)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    Man = await message.reply("♻️ `Processing...`")
    if not user_id:
        return await message.edit(
            "Provide User ID/Username or reply to user messages to unblock."
        )
    if user_id == client.me.id:
        return await Man.edit("anda stress harap segera minum obat.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Successfully Unblock** {umention}")


@Client.on_message(filters.command(["setname"], [".", "-", "^", "!", "?"]) & filters.me)
async def setname(client: Client, message: Message):
    Man = await message.reply("♻️ `Processing...`")
    if len(message.command) == 1:
        return await Man.edit(
            "Provide text to set as your telegram name."
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await Man.edit(f"**Successfully Changed Your Telegram Name To** `{name}`")
        except Exception as e:
            await Man.edit(f"**ERROR:** `{e}`")
    else:
        return await Man.edit(
            "Provide text to set as your telegram name."
        )


@Client.on_message(filters.command(["setbio"], [".", "-", "^", "!", "?"]) & filters.me)
async def set_bio(client: Client, message: Message):
    Man = await message.reply("♻️ `Processing...`")
    if len(message.command) == 1:
        return await Man.edit("Provide text to set as bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await Man.edit(f"**Successfully Changed your BIO to** `{bio}`")
        except Exception as e:
            await Man.edit(f"**ERROR:** `{e}`")
    else:
        return await Man.edit("Provide text to set as bio.")


@Client.on_message(filters.me & filters.command(["setpfp"], [".", "-", "^", "!", "?"]))
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.edit("**Your Profile Photo Has Been Successfully Changed.**")
    else:
        await message.edit(
            "`Reply to any photo to set as profile photo.`"
        )
        await sleep(3)
        await message.delete()


@Client.on_message(filters.me & filters.command(["vpfp"], [".", "-", "^", "!", "?"]))
async def view_pfp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id:
        user = await client.get_users(user_id)
    else:
        user = await client.get_me()
    if not user.photo:
        await message.edit("Profile photo not found!")
        return
    await client.download_media(user.photo.big_file_id, file_name=profile_photo)
    await client.send_photo(
        message.chat.id, profile_photo, reply_to_message_id=ReplyCheck(message)
    )
    await message.delete()
    if os.path.exists(profile_photo):
        os.remove(profile_photo)


add_command_help(
    "profile",
    [
        [".block", "Untuk memblokir pengguna telegram"],
        [".unblock", "Untuk membuka pengguna yang anda blokir"],
        [".setname", "Untuk Mengganti Nama Telegram."],
        [".setbio", "Untuk Mengganti Bio Telegram."],
        [
            ".setpfp",
            f"Balas Ke Gambar Ketik .setpfp Untuk Mengganti Foto Profil Telegram.",
        ],
        [".vpfp", "Untuk melihat foto profile pengguna saat ini."],
    ],
)
