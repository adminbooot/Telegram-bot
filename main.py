import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def start(message):
 bot.reply_to(message,f'''WELCOM IN BOT GET INFO USER INSTAGRAM ๐๐ฅ
SEND USER NOW ยป

ุงููุง ุจฺช ูู ุจูุช ุฌูุจ ูุนูููุงุช  ุงูุงูุณุชุบุฑุงู ๐๐ฅ
ุงุฑุณู ุงูููุฒุฑ ุงูุงู ยป

โโโโโโโโโโโโโโโโโโ
DEV:@CD_B5
CH:@IIIBIIl
''')
@bot.message_handler(func=lambda m:True)
def d(message):   
 user = message.text
 url = f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}"
 r = requests.get(url).json()
 try:
  na = r["results"]["name"]
  po = r["results"]["Posts"]
  fo = r["results"]["Followers"]
  fl = r["results"]["Following"]
  id = r["results"]["id"]
  cr = r["results"]["created date"]
  bot.send_message(message.chat.id,f'''HI โขุุ THIS IS ACC... INFO...
โโโโโโโโโโโโโโโโโโ
หน๐หผ USER โฃ {user}
หน๐ซฐหผ NAME โฃ {na}
หน๐บหผ POSTS โฃ {po}
หน๐ฅหผ FOLLOWERS โฃ {fo}
หน๐ปหผ FOLLOWING โฃ {fl}
หน๐หผ ID โฃ {id}
หนโ๏ธหผ DATE โฃ {cr}
โโโโโโโโโโโโโโโโโโ
หน๐งโ๐ปหผ DEV โฃ @CD_B5
หน๐งโ๐ฌหผ CH โฃ @IIIBIIl''')
 except:
     bot.send_message(message.chat.id,f'''NOT USER FOUND ๐
ูู ูุชู ุงูุนุซูุฑ ุนูุฆ ุงูููุฒุฑ ๐''')
bot.infinity_polling()

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://adminboot.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
