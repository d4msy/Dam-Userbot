# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# Dam-PyroBot

import html
import re


def cleanhtml(raw_html):
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext


def escape_markdown(text):
    """Helper function to escape telegram markup symbols."""
    escape_chars = r"\*_`\["
    return re.sub(r"([%s])" % escape_chars, r"\\\1", text)


def mention_html(user_id, name):
    return '<a href="tg://user?id={}">{}</a>'.format(user_id, html.escape(name))


def mention_markdown(user_id, name):
    return "[{}](tg://user?id={})".format(escape_markdown(name), user_id)
