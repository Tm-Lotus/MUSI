import asyncio

import os
import time
import requests
from config import USER_OWNER, OWNER_ID, SUPPORT_CHANNEL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AlexaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AlexaMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","زد إي","السورس", "سورس زد إي"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c4f9c850312c8891385a9.jpg",
        caption=f"""**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ . .
 [🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱](https://t.me/Source_Ze)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/ELHYBA"), 
                    
                
                    InlineKeyboardButton(
                        "‹ الدعم ›", url=f"https://t.me/ZeSupport"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/Source_Ze"),
                
        ],

            ]

        ),

    )

