

from pyrogram import Client, filters 
from database.users_chats_db import db
from info import RENAME_MODE

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if RENAME_MODE == False:
        return 
    caption = await client.ask(message.chat.id, "**Give Me A Caption To Set.\n\nAvailable Filling :-\n File Name: `{filename}`\n\nSize: `{filesize}`\n\nDuration: `{duration}`**")
    await db.set_caption(message.from_user.id, caption=caption.text)
    await message.reply_text("**Your Caption Successfully Saved**")

    
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    if RENAME_MODE == False:
        return 
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("**Sorry ! No Caption found...**")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**Your Caption deleted successfully**")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    if RENAME_MODE == False:
        return 
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Your Caption:-**\n\n`{caption}`")
    else:
       await message.reply_text("**Sorry ! No Caption found...**")
