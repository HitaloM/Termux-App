import os
from glob import glob

import pyrogram
from pyrogram.enums import ParseMode
from pyrogram.types import InputMediaDocument

short_rev = os.getenv("SHORT_REV")
long_rev = os.getenv("LONG_REV")
branch = os.getenv("BRANCH")
time = os.getenv("TIME")
apk_dir = os.getenv("APK_DIR_PATH")


with pyrogram.Client(
    "bot",
    os.getenv("API_ID"),
    os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN"),
    in_memory=True,
) as client:
    files = []
    for path in glob(f"{apk_dir}/*.apk", recursive=True):
        text: str = (
            f"**Branch:** [{branch}](https://github.com/termux/termux-app/tree/{branch})\n"
            f"**File:** ```{os.path.basename(path)}```\n"
            f"\nAPK Built with the [{short_rev}](https://github.com/termux/termux-app/commit/{long_rev}) commit (Commit made on {time})."
        )
        files.append(
            InputMediaDocument(media=path, caption=text, parse_mode=ParseMode.MARKDOWN)
        )

    client.send_media_group(
        chat_id=os.getenv("CHAT_ID"),
        media=files,
    )
