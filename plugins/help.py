from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt1 = f"📌 No playlist support. Just send the YouTube Url"
    helptxt2 = f"📌 Get the youtube url From @vid"
    helptxt3 = f"📌 Contact @RexZeal if you have any problems"

    await message.reply_text(helptxt1)
    await message.reply_text(helptxt2)
    await message.reply_text(helptxt3)
