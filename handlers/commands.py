import random
import json
import asyncio
from aiogram.types import Message
from data import config
from boot import bot, dp, types
from data.txt import START_MESSAGE, HELP_COMMAND, CHANGELOG_COMMAND, SOURCE_COMMAND
from kb.kb import ikb, ikb2

@dp.message_handler(commands=['start'])
async def start_command(message):
    if message.chat.id not in config.blackListChat:
        if message.from_user.id not in config.blackListUsers:
            await bot.send_message(chat_id=message.chat.id, text=START_MESSAGE, reply_markup=ikb)

@dp.message_handler(commands=['help'])
async def help_command(message):
    if message.chat.id not in config.blackListChat:
        if message.from_user.id not in config.blackListUsers:
            await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=['random'])
async def random_command(message):
    if message.chat.id not in config.blackListChat:
        if message.from_user.id not in config.blackListUsers:
            num = random.randint(1, 113)
            if num == 113:
                await message.answer(f"{num} жесть, отсылка?")
            else:
                await message.answer(f"{num}")

@dp.message_handler(commands=['source'])
async def source_command(message):
    await message.answer(f'{SOURCE_COMMAND}')

@dp.message_handler(commands=['photo'])
async def photo_command(message):
    if message.chat.id not in config.blackListChat:
        if message.from_user.id not in config.blackListUsers:    
            await bot.send_photo(chat_id=message.chat.id, photo="https://i.ytimg.com/vi/PkT0PJwy8mI/sddefault.jpg")

@dp.message_handler(commands=['changelog'])
async def changelog_command(message):
    if message.chat.id not in config.blackListChat:
        if message.from_user.id not in config.blackListUsers:
            await bot.send_message(chat_id=message.chat.id, text=CHANGELOG_COMMAND)

@dp.message_handler(commands=['MTEz'])
async def MTEz(message):
    if message.chat.id not in config.blackListChat:
        if message.from_user.id not in config.blackListUsers:
            await message.answer(message)

# command to get user information
@dp.message_handler(commands=['info'])
async def info_command(message):
    if message.chat.id not in config.blackListChat:
        if message.from_user.id not in config.blackListUsers:
            user_id = message.get_args()
            if not user_id:
                if message.reply_to_message:
                    await message.reply(f'ID: <code>{message.reply_to_message.from_user.id}</code> \nUsername: @{message.reply_to_message.from_user.username} \nlink: {message.reply_to_message.from_user.get_mention(as_html=True)}')
                else:
                    await message.answer(f'ID: <code>{message.from_user.id}</code> \nUsername: @{message.from_user.username} \nlink: {message.from_user.get_mention(as_html=True)}')
            else:
                        user_id = int(user_id)
                        user = await bot.get_chat(user_id)
                        info_message = (
                            f"ID: <code>{user.id}</code>\n"
                            f"Username: @{user.username}\n"
                            f"link: {user.get_mention(as_html=True)}"
                        )
                        await message.reply(info_message)

# that command formats text into JSON
@dp.message_handler(commands=['json'])
async def json_command(message):
    def remove_null(obj):
        if isinstance(obj, dict):
            return {k: remove_null(v) for k, v in obj.items() if v is not None}
        elif isinstance(obj, list):
            return [remove_null(item) for item in obj]
        else:
            return obj

    if message.text:
        message_data =  {
            "message_id": message.message_id,
            "from_user": {
                "id": message.from_user.id,
                "is_bot": message.from_user.is_bot,
                "is_premium": message.from_user.is_premium,
                "first_name": message.from_user.first_name,
                "last_name": message.from_user.last_name,
                "username": message.from_user.username,
                "language_code": message.from_user.language_code,
            },
            "chat": {
                "id": message.chat.id,
                "title": message.chat.title,
                "username": message.chat.username,
                "type": message.chat.type,
            },
            "date": message.date.strftime("%Y-%m-%d %H:%M:%S"),
            "text": message.text,
            "entities": [{
                "type": entity.type,
                "offset": entity.offset,
                "length": entity.length,
            } for entity in message.entities],

        }   

    message_data = remove_null(message_data)

    message_json = json.dumps(message_data, ensure_ascii=False, indent=2)

    await message.reply((f"""
nya, json \n
<code>{message_json}</code>
"""))

@dp.message_handler(commands=['ss'])
async def ss_command(message):
    response_text = " ".join(message.text.split()[1:]) or "<code>\u3164</code>"
    if message.from_user.id in config.whitelist:
    
        if message.reply_to_message:
        
            message.reply_to_message.reply(response_text)
        else:
            await bot.send_message(text=response_text, chat_id=message.chat.id)
    else:
        return

# I wrote this command when i was learning how to loging press on the inline button.
last_handler_executed = 0

@dp.message_handler(commands=['knopochki'])
async def knopochki_test_command(message):
    if message.chat.id not in config.blackListChat:
        if message.from_user.id not in config.blackListUsers:

            async def can_execute_handler() -> bool:
                global last_handler_executed
                current_time = asyncio.get_event_loop().time()
                if current_time - last_handler_executed >= 60:
                    last_handler_executed = current_time
                    return True
                return False 
            if await can_execute_handler():

                button = types.InlineKeyboardButton("Кошка!", callback_data='send_info')
                keyboard = types.InlineKeyboardMarkup().add(button)

                await message.reply("Кто такая <code>781589833</code>", reply_markup=keyboard)


# that commands add, delete, output, clear, and update information to JSON file
@dp.message_handler(commands=["output"])
async def output_data(message):
    data = read_data_from_json()
    if data:
        await message.answer("Текущие данные в JSON:")
        for name, age in data.items():
            await message.answer(f"{name}: {age}")
    else:
        await message.answer("тут ничего нет...")

@dp.message_handler(commands=["clear"])
async def clear_data(message):
    data = read_data_from_json()
    if data:
        write_data_to_json({})
        await message.answer("Все данные очищены")
    else:
        await message.answer("Уже пуст.")


@dp.message_handler(lambda message: message.text and message.text.startswith("/update"))
async def process_update_command(message):
    try:
        _, name, new_age = message.text.split(maxsplit=2)
        new_age = int(new_age)
        data = read_data_from_json()
        if name in data:
            data[name] = new_age
            write_data_to_json(data)
            await message.answer(f"Возраст для '{name}' обновлен.")
        else:
            await message.answer(f"Имя '{name}' не найдено.")
    except ValueError:
        await message.answer("Неверный формат.")

@dp.message_handler(lambda message: message.text and message.text.startswith("/delete"))
async def process_delete_command(message):
    try:
        _, name = message.text.split(maxsplit=1)
        data = read_data_from_json()
        if name in data:
            del data[name]
            write_data_to_json(data)
            await message.answer(f"Данные для '{name}' удалены.")
        else:
            await message.answer(f"Имя '{name}' не найдено.")
    except ValueError:
        await message.answer("Неверный формат.")

JSON_FILE_PATH = "data.json"


def read_data_from_json():
    try:
        with open(JSON_FILE_PATH, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}


def write_data_to_json(data):
    with open(JSON_FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

@dp.message_handler(content_types=types.ContentType.AUDIO)
async def voi(message: types.Message):
        file_id = message.audio.file_id
        file_info = await bot.get_file(file_id)
        file_path = file_info.file_path

        # Скачиваем файл
        file = await bot.download_file(file_path)

        await bot.send_voice(message.chat.id, file)

@dp.message_handler(lambda message: message.text and message.text.startswith("/add"))
async def process_add_command(message):
    try:
        _, name, age = message.text.split(maxsplit=2)
        age = int(age)

        data = read_data_from_json()
        data[name] = age
        write_data_to_json(data)
        await message.answer(f"Имя '{name}' и возраст '{age}' добавлены.")
    except ValueError:
        await message.answer("Неверный формат.")



#{}=-----[ Unused code for now ]=-----={}#

# @dp.message_handler(commands=['list'])
# async def list(message):
#      # Формируем список администраторов
#      admins_list = '\n'.join([f'{user_id}' for user_id in admin_id])
    
#      await message.reply(f'Список администраторов:\n{admins_list}')

# @dp.message_handler(commands=['alloff'])
# async def alloff_command(message):
#     if (message.from_user.id) in admin_id:
#         await message.delete()
#         alloffMessage = await bot.send_message(chat_id=message.chat.id, text='Хорошо, снимаю всех')
#         await bot.promote_chat_member(chat_id=message.chat.id, user_id=all_id, can_change_info=False, can_delete_messages=False, can_restrict_members=False, can_invite_users=False, can_pin_messages=False, can_promote_members=False,is_anonymous=False,can_manage_video_chats=False)
#         await asyncio.sleep(5)
#         await alloffMessage.delete
