from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

trainer = ListTrainer(chatbot)

trainer.train([
    "You are welcome for the follow.",
	"You're welcome.",
	"No problem.",
	"Thanks for the DM ;)",
	"Cool."
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('Thanks for the follow.')

print(response)