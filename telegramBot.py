#pylint:disable=E0611

import telebot
from nltk.chat.util import Chat
from reflections import my_reflections
from pairs import my_pairs, unknown
from no_accent import remove_accents

TOKEN = "Entrez votre TOKEN Telegram bot"
bot = telebot.TeleBot(TOKEN)
umaponBot = Chat(pairs=my_pairs, reflections=my_reflections)

while True:
	try :
		@bot.message_handler(commands=['start'])
		def start(message):
			bot.send_message(message.chat.id, "Bonjour, que aimeriez-vous savoir ?")
		
		@bot.message_handler(content_types=['text'])
		def receive(message):
			user = str(message.text)
			user = remove_accents(user)
			answer = umaponBot.respond(user)
			if answer is None:
				answer = unknown
			bot.send_message(message.chat.id, answer)
		bot.polling()
	except :
		pass	
