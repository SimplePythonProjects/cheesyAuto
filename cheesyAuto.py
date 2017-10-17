#!/usr/bin/python
#!/home/ubuntu/Cheesy_python3/venv/bin/python
import telebot
import random
from pickupLine import getPickupLine
from jokes import getJoke
from comic import getComic
from dirty import getDirtyLine

bot = telebot.TeleBot("410814681:AAEAsNsqywiZ4C8iFrwZbl-DdyEHUPmlcww")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	cid = message.chat.id
	bot.send_message(cid, "Commands : \n /comic \n /cheesy \n /dirty \n /nonstop \n /stop \n")

@bot.message_handler(commands=['joke'])
def send_joke(message):
	cid = message.chat.id
	joke = getJoke()
	bot.send_message(cid, joke)

@bot.message_handler(commands=['comic'])
def send_comic(message):
	cid = message.chat.id
	getComic()
	img = open('img.png', 'rb')
	bot.send_photo(cid, img)

@bot.message_handler(commands=['cheesy'])
def send_cheesy(message):
	cid = message.chat.id
	pickupLine = getPickupLine()
	bot.send_message(cid, pickupLine)

@bot.message_handler(commands=['dirty'])
def send_dirty(message):
	cid = message.chat.id
	dirtyLine = getDirtyLine()
	bot.send_message(cid, dirtyLine)

@bot.message_handler(commands=['nonstop'])
def set_chat_id(message):
	cid = message.chat.id
	global chatIdList
	if cid not in chatIdList:
		chatIdList.append(cid)
		print(chatIdList)
		bot.send_message(cid, "You will get non stop messages")
	else:
		bot.send_message(cid, "You are already receiving non stop message")

@bot.message_handler(commands=['stop'])
def unset_chat_id(message):
	cid = message.chat.id
	global chatIdList
	if(cid in chatIdList):
		chatIdList.remove(cid)
		print(chatIdList)
		bot.send_message(cid, "You wont get any message unless you type the commands")
	else:
		bot.send_message(cid, "You din't subscribe for non stop messages")
	
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	cid = message.chat.id
	bot.send_message(cid, "Try /help")

def sendgroupMessage():
	chatIdList = [-1001123624076]
	r_int = random.randint(0,2)
	if r_int == 0:
		getComic()
		img = open('img.png', 'rb')
		for id in chatIdList:
			bot.send_photo(id, img)
	elif r_int == 1:
		pickupLine = getPickupLine()
		for id in chatIdList:
			bot.send_message(id, pickupLine)
	else:
		dirtyLine = getDirtyLine()
		for id in chatIdList:
			bot.send_message(id, dirtyLine)

sendgroupMessage()
