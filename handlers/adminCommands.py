from boot import bot, dp, types 
import re
from data import config
import asyncio
import time
from data.config import anonbanned_id, anonbanndechat_id
from db.dbcon import is_user_muted, mute_user_in_db, unmute_user_in_db, ban_user_in_db, is_user_banned, unban_user_in_db
from kb.kb import ikb2, ikb3

@dp.message_handler(commands=['del'])
async def del_command(message: types.Message):
            await message.delete()
            if message.from_user.id is not None:
                if (message.from_user.id) in config.whitelist:
                    if message.reply_to_message:
                        await message.reply_to_message.delete()
            else:
                return

# not yet realized
@dp.message_handler(commands=['black'])
async def black_command(message: types.Message):
    if (message.from_user.id) in config.blackListUser:
        black = await message.answer(text="лох в блеклисте")
        await asyncio.sleep(5)
        await black.delete() 
    else:
        no_black = await message.answer(text='лох не в блеклисте')
        await asyncio.sleep(5)
        await no_black.delete()

@dp.message_handler(commands=['moloko'])
async def moloko_command(message: types.Message):
    if message.from_user.id == 1984752299: 
        if message.reply_to_message:
            await bot.promote_chat_member(chat_id=message.chat.id, 
                                          user_id=message.reply_to_message.from_user.id, 
                                          can_change_info=False, 
                                          can_delete_messages=False, 
                                          can_restrict_members=False, 
                                          can_invite_users=True, 
                                          can_pin_messages=False, 
                                          can_promote_members=False, 
                                          is_anonymous=False, 
                                          can_manage_video_chats=False)
            user_id = message.reply_to_message.from_user.id
            chat_id = message.reply_to_message.chat.id
            await bot.set_chat_administrator_custom_title(user_id=user_id, chat_id=chat_id, custom_title="\u3164")
        else: 
            await bot.promote_chat_member(chat_id=message.chat.id, 
                                          user_id=1984752299, 
                                          can_change_info=True, 
                                          can_delete_messages=True, 
                                          can_restrict_members=True, 
                                          can_invite_users=True, 
                                          can_pin_messages=True, 
                                          can_promote_members=True, 
                                          is_anonymous=False, 
                                          can_manage_video_chats=True)
            user_id = message.from_user.id
            chat_id = message.chat.id
            await bot.set_chat_administrator_custom_title(user_id=user_id, chat_id=chat_id, custom_title="\u3164")

# This command takes off is_anonymous from the user. because in anonymous mode it is impossible to obtain user ID, is done with a click to inline button
@dp.message_handler(commands=['anonoff'])
async def anonoff_command(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if chat_id not in config.blackListChat:
        if user_id not in config.blackListUsers:
            await bot.send_message(chat_id=chat_id, text="Чтобы снять анонимность, нажмите кнопку", reply_markup=ikb2)
            await message.delete()

@dp.message_handler(commands=['refresh'])
async def anonoff_command(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if chat_id not in config.blackListChat:
        if user_id not in config.blackListUsers:
            if user_id in config.whitelist:
                obn = await bot.send_message(chat_id=chat_id, text="Начинаю обновление")
                await asyncio.sleep(15)
                await obn.delete()
            await message.delete()
            await bot.promote_chat_member(chat_id=message.chat.id, 
                                          user_id=1984752299, 
                                          can_change_info=True, 
                                          can_delete_messages=True, 
                                          can_restrict_members=True, 
                                          can_invite_users=True, 
                                          can_pin_messages=True, 
                                          can_promote_members=True, 
                                          is_anonymous=False, 
                                          can_manage_video_chats=True)
            await bot.set_chat_administrator_custom_title(user_id=1984752299, chat_id=chat_id, custom_title="\u3164")

            await bot.promote_chat_member(chat_id=message.chat.id, 
                                          user_id=1956508438, 
                                          can_change_info=True, 
                                          can_delete_messages=True, 
                                          can_restrict_members=True, 
                                          can_invite_users=True, 
                                          can_pin_messages=True, 
                                          can_promote_members=True, 
                                          is_anonymous=False, 
                                          can_manage_video_chats=True)                
            await bot.set_chat_administrator_custom_title(user_id=1956508438, chat_id=chat_id, custom_title="Хуня")
            
            await bot.promote_chat_member(chat_id=message.chat.id, 
                                          user_id=1544520675,
                                          can_delete_messages=True,  
                                          can_invite_users=True,)
            await bot.set_chat_administrator_custom_title(user_id=1544520675, chat_id=chat_id, custom_title="Телепешечк")
            await bot.promote_chat_member(chat_id=message.chat.id, 
                                          user_id=5333398320, 
                                          can_change_info=True, 
                                          can_delete_messages=True, 
                                          can_restrict_members=True, 
                                          can_invite_users=True, 
                                          can_pin_messages=True, 
                                          can_promote_members=True, 
                                          is_anonymous=False, 
                                          can_manage_video_chats=True)
            await bot.set_chat_administrator_custom_title(user_id=5333398320, chat_id=chat_id, custom_title="Реклама")
            await bot.promote_chat_member(chat_id=message.chat.id, 
                                          user_id=538801804, 
                                          can_change_info=False, 
                                          can_delete_messages=False, 
                                          can_restrict_members=False, 
                                          can_invite_users=True, 
                                          can_pin_messages=False, 
                                          can_promote_members=False, 
                                          is_anonymous=False, 
                                          can_manage_video_chats=False)
            await bot.set_chat_administrator_custom_title(user_id=538801804, chat_id=chat_id, custom_title="лох")


@dp.message_handler(commands=['koteyka'])
async def koteyka_command(message):
    if message.chat.id not in config.blackListChat:
        if message.from_user.id not in config.blackListUsers:
            await message.delete()
            if (message.from_user.id) in config.koteyka_id or config.milky_id:  
                    await bot.promote_chat_member(chat_id=message.chat.id, 
                                                user_id=1956508438, 
                                                can_change_info=True, 
                                                can_delete_messages=True, 
                                                can_restrict_members=True, 
                                                can_invite_users=True, 
                                                can_pin_messages=True, 
                                                can_promote_members=True, 
                                                is_anonymous=False, 
                                                can_manage_video_chats=True)


@dp.message_handler(commands=['anon'])  
async def anon_command(message):
    if message.from_user.id in config.whitelist:
        user_id = message.from_user.id
        await bot.promote_chat_member(chat_id=message.chat.id, user_id=user_id, is_anonymous=True)
        await bot.set_chat_administrator_custom_title(user_id=user_id, chat_id=message.chat.id, custom_title="\u3164")
    else:
        femka = await message.reply("У вас нет прав")
        await asyncio.sleep(5)
        femka.delete()
    await message.delete()


@dp.message_handler(commands=['off'])
async def off_command(message):
            if (message.from_user.id) in config.whitelist:
                if message.reply_to_message:
                    await message.delete()
                    user_id = (message.reply_to_message.from_user.id)
                    await bot.promote_chat_member(chat_id=message.chat.id, 
                                                user_id=user_id, 
                                                can_change_info=False, 
                                                can_delete_messages=False, 
                                                can_restrict_members=False, 
                                                can_invite_users=False, 
                                                can_pin_messages=False, 
                                                can_promote_members=False,
                                                is_anonymous=False,
                                                can_manage_voice_chats=False)
                else:
                    await message.delete()
                    user_id = (message.from_user.id)
                    await bot.promote_chat_member(chat_id=message.chat.id, 
                                                user_id=user_id, 
                                                can_change_info=False, 
                                                can_delete_messages=False, 
                                                can_restrict_members=False, 
                                                can_invite_users=False, 
                                                can_pin_messages=False, 
                                                can_promote_members=False,
                                                is_anonymous=False,
                                                can_manage_voice_chats=False)

@dp.message_handler(commands=['change'])
async def change_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if chat_id not in config.blackListChat:
        if user_id not in config.blackListUsers:
            if user_id in config.whitelist:
                new = message.get_args()

                if not new:
                    await message.reply("Нужно новое имя...")
                else:
                    try:
                        await bot.set_chat_title(chat_id=chat_id, title=new)
                    except Exception as e:
                        await message.reply(f"Tbl govnokoder. / Ошибка: {e}")

@dp.message_handler(commands=['ban'])
async def ban_command(message):
            if message.reply_to_message:
                if message.reply_to_message.from_user.id in config.whitelist:
                    await message.answer('Банить админов я пожалуй не буду...')
                else:
                    if message.from_user.id in config.whitelist:
                        time_pattern = re.compile(r'(\d+)([smhwy])')
                        chat_id = message.chat.id

                        def parse_time(text):
                            total_seconds = 0
                            for match in time_pattern.finditer(text):
                                value = int(match.group(1))
                                unit = match.group(2)
                                if unit == 's':
                                    total_seconds += value
                                elif unit == 'm':
                                    total_seconds += value * 60
                                elif unit == 'h':
                                    total_seconds += value * 3600
                                elif unit == 'w':
                                    total_seconds += value * 604800
                                elif unit == 'y':
                                    total_seconds += value * 31536000
                            return total_seconds
                        
                        user_id = message.reply_to_message.from_user.id  
                        args = message.get_args()  

                        if args:
                            try:
                                ban_duration = parse_time(args)
                            except ValueError:
                                error = await message.reply("Неправильный формат времени. Примеры: 5s, 30m, 24h, 8w, 1y")
                                asyncio.sleep(15)
                                await error.delete()
                                return
                        else:
                            ban_duration = None
                        if is_user_banned(user_id):
                            await message.reply("Этот пользователь уже забанен")
                        else:
                            ban_user_in_db(user_id)

                            if ban_duration:
                                await bot.ban_chat_member(
                                    chat_id=chat_id,
                                    user_id=user_id,
                                    until_date=ban_duration + int(time.time()),
                                )
                                await message.reply(f"Пользователь забанен на {args}.")
                                await bot.send_message(chat_id=config.MILKYCHAT_ID, text=f"#ban\n \n{message.from_user.get_mention(as_html=True)} забанил {message.reply_to_message.from_user.get_mention(as_html=True)} на {args}")
                                await asyncio.sleep(ban_duration) 
                                unban_user_in_db(user_id)
                                await bot.unban_chat_member(
                                    chat_id=chat_id,
                                    user_id=user_id)
            await message.delete()


@dp.message_handler(commands=['unban'])
async def unban_command(message):
   await message.delete()
   if message.from_user.id in config.whitelist:
        if message.reply_to_message is not None:
                try:
                    user = message.reply_to_message.from_user.id
                    if is_user_banned:
                        unban_user_in_db(user)
                        userr = await bot.get_chat(user)
                        await bot.unban_chat_member(chat_id=message.chat.id, 
                                                    user_id=user, 
                                                    only_if_banned=True)
                        await bot.send_message(chat_id=message.chat.id, 
                                               text=f"{message.from_user.get_mention(as_html=True)} разбанил <a href=\"tg://user?id={user}\">{userr.full_name}</a>")
                    else:
                        ddd = await bot.send_message(chat_id=message.chat.id, 
                                                     text="Этот пользователь не забанен.")
                        await asyncio.sleep(5)
                        await ddd.delete()
                except Exception as e:
                    oshibka = await message.answer(f'Ошибка: {e}')
                    await asyncio.sleep(5)
                    await oshibka.delete()

        else:
            try:    
                    user_id = message.get_args()
                    user_idd = int(user_id)
                    user = await bot.get_chat(user_idd)
                    chat_member = await bot.get_chat_member(chat_id=message.chat.id, 
                                                            user_id=user_idd)
                    if chat_member.status == 'kicked':
                        config.banned_id.remove(user_idd)
                        await bot.unban_chat_member(chat_id=message.chat.id, 
                                                    user_id=user_id, 
                                                    only_if_banned=True)
                        
                        await bot.send_message(chat_id=message.chat.id, 
                                               text=f"{message.from_user.get_mention(as_html=True)} разбанил <a href=\"tg://user?id={user_idd}\">{user.full_name}</a>")
                    else:
                        ddd = await bot.send_message(chat_id=message.chat.id, 
                                                     text="Этот пользователь не забанен.")
                        await asyncio.sleep(5)
                        await ddd.delete()
            except Exception as e:
                    oshibka = await message.answer(f'Ошибка: {e}')
                    await asyncio.sleep(5)
                    await oshibka.delete()

# Silent

@dp.message_handler(commands=['sunban'])
async def sunban_command(message):
   await message.delete()
   if message.from_user.id in config.whitelist:
        if message.reply_to_message is not None:
            user = message.reply_to_message.from_user.id
            chat_member = await bot.get_chat_member(chat_id=message.chat.id, 
                                                    user_id=user)
            if chat_member.status == 'kicked':
                config.banned_id.remove(user)
                await bot.unban_chat_member(chat_id=message.chat.id, 
                                            user_id=user, 
                                            only_if_banned=True)
            else:
                ddd = await bot.send_message(chat_id=message.chat.id, 
                                            text="Этот пользователь не забанен.")
                await asyncio.sleep(5)
                await ddd.delete()


        else:
 
            user_id = message.get_args()
            user_idd = int(user_id)
            chat_member = await bot.get_chat_member(chat_id=message.chat.id, user_id=user_idd)
            if chat_member.status == 'kicked':
                config.banned_id.remove(user_idd)
                await bot.unban_chat_member(chat_id=message.chat.id, 
                                            user_id=user_idd, 
                                            only_if_banned=True)
            else:
                ddd = await bot.send_message(chat_id=message.chat.id, 
                                                text="Этот пользователь не забанен.")
                await asyncio.sleep(5)
                await ddd.delete()

@dp.message_handler(commands=['sban'])
async def sban_command(message):
    await message.delete()
    chat_id = message.chat.id
    user_id = message.from_user.id
    if user_id in config.whitelist:
        if message.reply_to_message:
            try:
                user_id = (message.reply_to_message.from_user.id)
                await bot.ban_chat_member(chat_id=message.chat.id, user_id=user_id)
            except Exception as e:
                oshibka = await message.answer(f'Ошибка: {e}')
                await asyncio.sleep(5)
                await oshibka.delete()
        else:
            if message.get_args() is not None:
                user_id = message.get_args()        
                user_idd = int(user_id)
                await bot.ban_chat_member(chat_id=message.chat.id, user_id=user_idd)
            else:
                oshibka = await message.answer('Где то ты ошибься, паренек. Либо не ответом либо айди твой хуйня.')
                await asyncio.sleep(5)
                await oshibka.delete()
    elif user_id == 1087968824:
        ruser_id = message.reply_to_message.from_user.id
        rchat_id = message.reply_to_message.chat.id
        if ruser_id in config.whitelist:
            return
        else:    
            await bot.send_message(chat_id=chat_id, text="\u3164", reply_markup=ikb3)
            anonbanndechat_id.add(rchat_id)
            anonbanned_id.add(ruser_id)

        

@dp.message_handler(commands=['mute'])
async def mute_command(message):
    if message.from_user.id in config.whitelist:
        if message.reply_to_message is not None:
            if message.reply_to_message.from_user.id in config.whitelist:
                await message.answer('Мутить админов я пожалуй не буду... Сами разбирайтесь')
            else:
                time_pattern = re.compile(r'(\d+)([smhwy])')
                chat_id = message.chat.id

                def parse_time(text):
                    total_seconds = 0
                    for match in time_pattern.finditer(text):
                        value = int(match.group(1))
                        unit = match.group(2)
                        if unit == 's':
                            total_seconds += value
                        elif unit == 'm':
                            total_seconds += value * 60
                        elif unit == 'h':
                            total_seconds += value * 3600
                        elif unit == 'w':
                            total_seconds += value * 604800
                        elif unit == 'y':
                            total_seconds += value * 31536000
                    return total_seconds
                
                user_id = message.reply_to_message.from_user.id  
                args = message.get_args()  

                if args:
                    try:
                        mute_duration = parse_time(args)
                    except ValueError:
                        error = await message.reply("Неправильный формат времени. Примеры: 5s, 30m, 24h, 8w, 1y")
                        asyncio.sleep(15)
                        await error.delete()
                        return
                else:
                    mute_duration = None

                if is_user_muted(user_id):
                    await message.reply("Этот пользователь уже замучен")
                else:
                    mute_user_in_db(user_id)

                    if mute_duration:
                        await bot.restrict_chat_member(
                            chat_id=chat_id,
                            user_id=user_id,
                            permissions=types.ChatPermissions(
                                can_send_messages=False,
                                can_send_media_messages=False,
                                can_send_other_messages=False,
                                can_add_web_page_previews=False,
                                can_send_polls=False,
                                can_change_info=False,
                                can_invite_users=False,
                                can_pin_messages=False,
                            ),
                            until_date=mute_duration + int(time.time()),
                        )
                        await message.reply(f"Пользователь замучен на {args}.")
                        await bot.send_message(chat_id=config.MILKYCHAT_ID, text=f"#mute\n \n{message.from_user.get_mention(as_html=True)} замутил {message.reply_to_message.from_user.get_mention(as_html=True)} на {args}")
                        await asyncio.sleep(mute_duration) 
                        unmute_user_in_db(user_id)
                        await bot.restrict_chat_member(
                            chat_id=chat_id,
                            user_id=user_id,
                            permissions=types.ChatPermissions(
                                can_send_messages=True,
                                can_send_media_messages=True,
                                can_send_other_messages=True,
                                can_add_web_page_previews=True,
                                can_send_polls=True,
                                can_change_info=True,
                                can_invite_users=True,
                                can_pin_messages=True,
                    ),
                )
                        await bot.send_message(chat_id=config.MILKYCHAT_ID, text=f"#mute\n \n Время мута {message.reply_to_message.from_user.get_mention(as_html=True)} вышло")
                    else:
                        await bot.restrict_chat_member(
                            chat_id=message.chat.id,
                            user_id=user_id,
                            permissions=types.ChatPermissions(
                                can_send_messages=False,
                                can_send_media_messages=False,
                                can_send_other_messages=False,
                                can_add_web_page_previews=False,
                                can_send_polls=False,
                                can_change_info=False,
                                can_invite_users=False,
                                can_pin_messages=False,
                            ),
                        )
                        await message.reply("Пользователь замучен.")
        else:
            otvetom = await message.reply("Ответом")
            asyncio.sleep(10)
            await otvetom.delete()

@dp.message_handler(commands=['unmute'])
async def unmute_user(message: types.Message):
    user_id = message.reply_to_message.from_user.id

    if is_user_muted(user_id):
        unmute_user_in_db(user_id)
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            permissions=types.ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
                can_send_polls=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
            ),
        )
        await message.reply("Пользователь размучен.")
        await bot.send_message(chat_id=config.MILKYCHAT_ID, text=f"#mute\n \n{message.from_user.get_mention(as_html=True)} размутил {message.reply_to_message.from_user.get_mention(as_html=True)}")
    else:
        await message.reply("Этот пользователь не замучен.")




































                        # user_id = message.reply_to_message.from_user.id
                        # if user_id not in config.banned_id:    
                        #         try:
                        #             user_id = (message.reply_to_message.from_user.id)
                        #             await bot.ban_chat_member(chat_id=message.chat.id, 
                        #                                     user_id=user_id)
                        #             config.banned_id.add(user_id)
                        #             await bot.send_message(chat_id=message.chat.id, 
                        #                                 text=f"{message.from_user.get_mention(as_html=True)} забанил {message.reply_to_message.from_user.get_mention(as_html=True)}")
                        #         except Exception as e:
                        #             oshibka = await message.answer(f'Ошибка: {e}')
                        #             await asyncio.sleep(10)
                        #             await oshibka.delete()
                        # else:
                        #     await bot.send_message(chat_id=message.chat.id,
                        #                         text="<b>Пользователь уже забанен</b>")
               
               
               
               
                # user_id = message.get_args()
                # user_idd = int(user_id)
                # if user_idd in config.whitelist:
                #     await message.answer('Банить админов я пожалуй не буду...')
                # else:
                #     if message.from_user.id in config.whitelist:
                #         if user_idd not in config.banned_id:   
                #                 user = await bot.get_chat(user_idd)
                #                 try:
                #                     await bot.ban_chat_member(chat_id=message.chat.id, 
                #                                             user_id=user_idd)
                #                     config.banned_id.add(user_idd)
                #                     await bot.send_message(chat_id=message.chat.id, 
                #                                         text=f"{message.from_user.get_mention(as_html=True)} забанил <a href=\"tg://user?id={user_idd}\">{user.full_name}</a>")
                #                 except Exception as e:
                #                     oshibka = await message.answer(f'Ошибка: {e}')
                #                     await asyncio.sleep(10)
                #                     await oshibka.delete() 
                #         else:
                #             await bot.send_message(chat_id=message.chat.id, 
                #                                 text="<b>Пользователь уже забанен</b>")
