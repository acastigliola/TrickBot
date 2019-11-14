from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

trainer = ListTrainer(chatbot)

trainer.train([
    "Nice.",
	"I been programming all day.",
	"You code?"
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('Not often and usually more hardware.')

print(response)