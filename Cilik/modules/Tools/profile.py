import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from Cilik.helpers.PyroHelpers import ReplyCheck
from Cilik.modules.Ubot.help import add_command_help
from Cilik.utils.misc import extract_user

flood = {}
profile_photo = "ProjectMan/modules/cache/pfp.jpg"


@Client.on_message(filters.command(["block"], [".", "-", "^", "!", "?"]) & filters.me)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    Man = await message.reply("💈 `Processing...`")
    if not user_id:
        return await message.edit(
            "Berikan User ID/Username atau reply pesan pengguna untuk membuka blokir."
        )
    if user_id == client.me.id:
        return await Man.edit("anda stress harap segera minum obat.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Berhasil Memblokir** {umention}")


@Client.on_message(filters.command(["unblock"], [".", "-", "^", "!", "?"]) & filters.me)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    Man = await message.reply("💈 `Processing...`")
    if not user_id:
        return await message.edit(
            "Berikan User ID/Username atau reply pesan pengguna untuk membuka blokir."
        )
    if user_id == client.me.id:
        return await Man.edit("anda stress harap segera minum obat.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Berhasil Membuka Blokir** {umention}")


@Client.on_message(filters.command(["setname"], [".", "-", "^", "!", "?"]) & filters.me)
async def setname(client: Client, message: Message):
    Man = await message.reply("💈 `Processing...`")
    if len(message.command) == 1:
        return await Man.edit(
            "Berikan teks untuk ditetapkan sebagai nama telegram anda."
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await Man.edit(f"**Berhasil Mengubah Nama Telegram anda Menjadi** `{name}`")
        except Exception as e:
            await Man.edit(f"**ERROR:** `{e}`")
    else:
        return await Man.edit(
            "Berikan teks untuk ditetapkan sebagai nama telegram anda."
        )


@Client.on_message(filters.command(["setbio"], [".", "-", "^", "!", "?"]) & filters.me)
async def set_bio(client: Client, message: Message):
    Man = await message.reply("💈 `Processing...`")
    if len(message.command) == 1:
        return await Man.edit("Berikan teks untuk ditetapkan sebagai bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await Man.edit(f"**Berhasil Mengubah BIO anda menjadi** `{bio}`")
        except Exception as e:
            await Man.edit(f"**ERROR:** `{e}`")
    else:
        return await Man.edit("Berikan teks untuk ditetapkan sebagai bio.")


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
        await message.edit("**Foto Profil anda Berhasil Diubah.**")
    else:
        await message.edit(
            "`Balas ke foto apa pun untuk dipasang sebagai foto profile`"
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
        await message.edit("Foto profil tidak ditemukan!")
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
