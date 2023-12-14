from boot import dp, types, bot
from aiogram.types import CallbackQuery
import logging
from data.config import MILKYCHAT_ID, whitelist, anonbanndechat_id, anonbanned_id

@dp.callback_query_handler(text_contains="anonoff")
async def callback_anonoff(call: CallbackQuery):     
    callback_data = call.data
    logging.info(f"call = {callback_data}")
    user_id = call.from_user.id
    chat_id = MILKYCHAT_ID
    if user_id == 1984752299:
                await bot.promote_chat_member(chat_id=chat_id, 
                                          user_id=user_id, 
                                          can_change_info=True, 
                                          can_delete_messages=True, 
                                          can_restrict_members=True, 
                                          can_invite_users=True, 
                                          can_pin_messages=True, 
                                          can_promote_members=True, 
                                          is_anonymous=False, 
                                          can_manage_video_chats=True)
                await bot.set_chat_administrator_custom_title(user_id=user_id, chat_id=chat_id, custom_title="\u3164")
    elif user_id == 1956508438:
                await bot.promote_chat_member(chat_id=chat_id, 
                                          user_id=user_id, 
                                          can_change_info=True, 
                                          can_delete_messages=True, 
                                          can_restrict_members=True, 
                                          can_invite_users=True, 
                                          can_pin_messages=True, 
                                          can_promote_members=True, 
                                          is_anonymous=False, 
                                          can_manage_video_chats=True)                
                await bot.set_chat_administrator_custom_title(user_id=user_id, chat_id=chat_id, custom_title="Хуня")
    elif user_id == 1544520675:
                await bot.promote_chat_member(chat_id=chat_id, 
                                          user_id=user_id,
                                          can_delete_messages=True,  
                                          can_invite_users=True,)
                await bot.set_chat_administrator_custom_title(user_id=user_id, chat_id=chat_id, custom_title="Телепешечк")
    elif user_id == 5333398320:
                await bot.promote_chat_member(chat_id=chat_id, 
                                          user_id=user_id, 
                                          can_change_info=True, 
                                          can_delete_messages=True, 
                                          can_restrict_members=True, 
                                          can_invite_users=True, 
                                          can_pin_messages=True, 
                                          can_promote_members=True, 
                                          is_anonymous=False, 
                                          can_manage_video_chats=True)
                await bot.set_chat_administrator_custom_title(user_id=user_id, chat_id=chat_id, custom_title="Реклама")
    await call.message.delete()

@dp.callback_query_handler(lambda query: query.data == 'send_info')
async def handle_inline_button_click1(query: types.CallbackQuery):
    user_id = query.from_user.id
    user_username = query.from_user.username
    get_mention = query.from_user.get_mention(as_html=True)
    await query.message.delete()
    
    await bot.send_message(-1001873458430, f"Пользователь {get_mention}, <code>{user_id}</code> нажал инлайн кнопку и ответил правильно")

    await query.answer("Вы ответили верно!", show_alert=True)

@dp.callback_query_handler(text_contains="anonban")
async def callback_anonoff(call: CallbackQuery):     
    callback_data = call.data
    logging.info(f"call = {callback_data}")
    user_id = call.from_user.id
    if user_id in whitelist:
            ruser_id = int(anonbanned_id)
            rchat_id = anonbanndechat_id
            await bot.ban_chat_member(ruser_id, rchat_id)