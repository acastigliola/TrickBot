from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

trainer = ListTrainer(chatbot)

trainer.train([
    "I know what that is lol",
    "lol",
	"ah lulz",
	"who is the lulz on?",
	"Orly?",
	"srs bsns...",
	"fuck off. kidding. lulz..",
	"who you troll'n bro?",
	"lol",
	"looooooooooooool",
	"You getting the feels?",
	"Whatever bro. :)",
	"Heh.",
	"funny.",
	"Funny.",
	"Too funny.",
	"That is too funny.",
	"Please troll @Lucky225 and not L0ra.",
	"Whatever.",
	"lulz.",
	"looool.",
	"MAX LULX.",
	"hahahahahahahahahaha.",
	"hahahahaha.",
	"hahaha.",
	"haha.",
	"ha.",
	"HA!.",
	"LOOOOL.",
	"LOOOL.",
	"LOL.",
	"Lulz.",
	"LULZ.",
	"LULZ!"
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('Troll.')

print(response)