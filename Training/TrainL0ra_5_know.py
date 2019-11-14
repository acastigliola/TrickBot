from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

trainer = ListTrainer(chatbot)

trainer.train([
    "Do you?",
    "Not sure. lol.",
	"ah lulz",
	"who is the lulz on?",
	"Orly?",
	"srs bsns...",
	"fuck off. kidding. lulz..",
	"who you troll'n bro?",
	"who wants to know?",
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('know')

print(response)