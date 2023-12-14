from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb = InlineKeyboardMarkup(row_width=1)
ib1 = InlineKeyboardButton(text='MilkyRoxxx🧑‍💻',url='t.me/kiddie113')
ikb.add(ib1)

ikb2 = InlineKeyboardMarkup(row_width=1)
ib21 = InlineKeyboardButton(text='Снять анонимность', callback_data='anonoff')
ikb2.add(ib21)

ikb3 = InlineKeyboardMarkup(row_width=1)
ib31 = InlineKeyboardButton(text='\u3164', callback_data="anonban")
ikb3.add(ib31)