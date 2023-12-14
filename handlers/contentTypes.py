from boot import dp, types, bot

@dp.message_handler(content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def on_user_leave_chat(message: types.Message):
    global ssban
    await message.delete()

    await bot.send_message(chat_id=message.chat.id, text=f'{message.left_chat_member.get_mention(as_html=True)} вышел из чата')

@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def on_new_chat_members(message: types.Message):
    await message.delete()
    for new_member in message.new_chat_members:
        if new_member.is_bot and (await bot.get_chat_member(message.chat.id, message.from_user.id)).can_restrict_members:
            admin_mention = message.from_user.get_mention(as_html=True)
            bot_mention = new_member.get_mention(as_html=True)
            welcome_message = f"{admin_mention} добавил {bot_mention}"
            await message.answer(welcome_message)
        else:
            await message.answer(f"Добро пожаловать - {message.from_user.get_mention(as_html=True)}")


#{}=-----[ Unused code for now ]=-----={}#

# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def phototest(message: types.Message):
#     largest_photo = message.photo[-1]
#     file_id = largest_photo.file_id
#     file_unique_id = largest_photo.file_unique_id
#     width = largest_photo.width
#     height = largest_photo.height
#     file_size = largest_photo.file_size

#     await message.reply(f"nya, phototest:\n"
#                         f"<code>File ID:</code><code> \n{file_id}</code>\n"
#                         f"<code>File Unique ID: {file_unique_id}</code>\n"
#                         f"<code>Width: {width}\n</code>"
#                         f"<code>Height: {height}</code>\n"
#                         f"<code>File Size: {file_size}</code>")