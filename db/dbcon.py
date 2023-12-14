import sqlite3
import asyncio
from boot import types, dp, bot
import time
from data import config

conn = sqlite3.connect('gate.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS banned_users (
        user_id INTEGER PRIMARY KEY
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS muted_users (
        user_id INTEGER PRIMARY KEY
    )
''')

conn.commit()

def ban_user_in_db(user_id):
    cursor.execute("INSERT INTO banned_users (user_id) VALUES (?)", (user_id,))
    conn.commit()

def unban_user_in_db(user_id):
    cursor.execute("DELETE FROM banned_users WHERE user_id=?", (user_id,))
    conn.commit()

def is_user_banned(user_id):
    cursor.execute("SELECT * FROM banned_users WHERE user_id=?", (user_id,))
    return cursor.fetchone() is not None

def mute_user_in_db(user_id):
    cursor.execute("INSERT INTO muted_users (user_id) VALUES (?)", (user_id,))
    conn.commit()

def unmute_user_in_db(user_id):
    cursor.execute("DELETE FROM muted_users WHERE user_id=?", (user_id,))
    conn.commit()

def is_user_muted(user_id):
    cursor.execute("SELECT * FROM muted_users WHERE user_id=?", (user_id,))
    return cursor.fetchone() is not None

