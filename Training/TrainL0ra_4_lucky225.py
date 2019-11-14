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
	"lucky22who?",
	"I know lucky225. He writes for 2600. He is also a media whore..",
	"Lucky is a media whore... Just say'n..",
	"Lucky and Linda are my favorite blag and IG..",
	"who wants to know?",
	"oh... you mean torch..."
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('lucky225')

print(response)