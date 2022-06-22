from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message
import os
from pyrogram.types import CallbackQuery
from pyrogram.types import ChatPermissions
from pyrogram.types import ReplyKeyboardMarkup

bot=Client(
    "Emo Deckstop Bot",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

#---------Start Buttons & Message------------#
START_MG = "Im Emo Deckstop Official State Bot!"
START_BTN = [
            [
                InlineKeyboardButton('HELP', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton(' SUPPORT', url='https://t.me/Emo_Bot_Support'),
                InlineKeyboardButton('📣 CHANNEL', url='https://t.me/AboutRishmika'),
                InlineKeyboardButton(' CREATOR', url='https://t.me/ImRishmika')
            ],
            [
                InlineKeyboardButton('NIGHT VISSION BOT LIST', callback_data="BOT_CALLBACK")
            ]
        ]

#--------------------Start Bot---------------------------#
@bot.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = START_MG
    reply_markup = InlineKeyboardMarkup(START_BTN)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
#------------HELP CALLBACK QUERY-----------#
HELP_MESSAGE = """What Can I do ?
➠ ban & unban user
➠ mute & unmute user
➠ kick a member
Available Commands
/start - Checking Bot Online
/help - all helps
/ban - ban a user
/unban - unban a user
/mute - mute a user
/unmute - unmute a user
/kick - kick users
/listbots - all available ™Night Vission Bots"""
HELP_BUTTONS = [
[InlineKeyboardButton('BACK', callback_data="BACK_MENU")]
]

@bot.on_callback_query(filters.regex("HELP_CALLBACK"))
async def helpmenu(_, query: CallbackQuery):
    await query.edit_message_text(
     text = HELP_MESSAGE,
     reply_markup = HELP_BUTTONS,
     disable_web_page_preview=True
    )
#----------------menu backcallbac----------------#
@bot.on_callback_query(filters.regex("BACK_MENU"))
async def startmenu(_, query: CallbackQuery):
    await query.edit_message_text(
     text = START_MG,
     reply_markup = START_BTN,
     disable_web_page_preview=True
    )
#-------------Bot List Callback---------------------#
@bot.on_callback_query(filters.regex("BOT_CALLBACK"))
async def botlist(_, query: CallbackQuery):
    await query.edit_message_text(
     text = BOT_LIST_MG,
     reply_markup = REPLY_BUTTONS,
     disable_web_page_preview=True
    )
#-------------BOT LIST CALLBACK--------------#
BOT_LIST_MG = "Chek Bellow All Emo Deckstop Bot Catogories"
REPLY_BUTTONS = ReplyKeyboardMarkup(
      [
            ["🎧Voice Chat"],
            ["Social"],
            ["Group Manager"],
            ["Tools & Helps"]
           
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    
#Buttons Replys
SFT = "This Is Vc bots"

@bot.on_message(filters.command('listbots'))
def listbots(bot, message):
	text = BOT_LIST_MG
	reply_markup = REPLY_BUTTONS
	message.reply(
	text=text,
	reply_markup=reply_markup
)
@bot.on_message(filters.regex("🎧Voice Chat"))
def reply_to_VoiceChat(bot, message):
	text = SFT,
	message.reply(
	text=text
) 
	
#kick a user ©Emo Deckstop Bot™ 2022 All rights Resived ✓
@bot.on_message(filters.command('kick') & filters.group)
def kick(bot, message):
            bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Go out Side"
)
#ban user ©Emo Deckstop Bot™ 2022 All rights Resived ✓
@bot.on_message(filters.command('ban') & filters.group)
def ban(bot, message):
            bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Fu*k off! \-_-/ You banned."
)
#unban user  ©Emo Deckstop Bot™ 2022 All Rights Resived✓
@bot.on_message(filters.command('unban') & filters.group)
def unban(bot, message):
            bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Unbanned! Come here!"
)

#mute user !  ©Emo Deckstop Bot™ 2022 All Rights Resived✓
@bot.on_message(filters.command('mute') & filters.group)
def mute(bot, message):
            bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Muted !"
)
#unmute user! ©Emo Deckstop Bot™ 2022 All Rights Resived✓

@bot.on_message(filters.command('unmute') & filters.group)
def unmute(bot, message):
            bot.unrestrict_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Unmuted You Can Send massage Now!"
)
            
            
print("</>Emo INDUSTRY</>")
bot.run()
