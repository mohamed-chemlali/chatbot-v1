from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 

bot = ChatBot('Bot') 

bot.set_trainer(ListTrainer) 

data = open('conversation.txt','r').readlines()

bot.train(data) 

while True:
	message = input('You:')
	
	reply = bot.get_response(message)
	print('ChatBot :',reply)
	
