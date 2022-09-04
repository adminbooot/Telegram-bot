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
 bot.reply_to(message,f'''WELCOM IN BOT GET INFO USER INSTAGRAM 😈🔥
SEND USER NOW »

اهلا بڪ في بوت جلب معلومات  الانستغرام 😈🔥
ارسل اليوزر الان »

○●○●○●○●○●○●○●○●○●
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
  bot.send_message(message.chat.id,f'''HI •؍؍ THIS IS ACC... INFO...
○●○●○●○●○●○●○●○●○●
˹💁˼ USER ‣ {user}
˹🫰˼ NAME ‣ {na}
˹🗺˼ POSTS ‣ {po}
˹👥˼ FOLLOWERS ‣ {fo}
˹🚻˼ FOLLOWING ‣ {fl}
˹🆔˼ ID ‣ {id}
˹⌛️˼ DATE ‣ {cr}
○●○●○●○●○●○●○●○●○●
˹🧑‍💻˼ DEV ‣ @CD_B5
˹🧑‍🔬˼ CH ‣ @IIIBIIl''')
 except:
     bot.send_message(message.chat.id,f'''NOT USER FOUND 💔
لم يتم العثور علئ اليوزر 💔''')
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
