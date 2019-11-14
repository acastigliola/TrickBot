from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

trainer = ListTrainer(chatbot)

trainer.train([
    "Ah got ya.",
	"What you up to?",
	"Sounds like big fun :)"
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('Breakfast.')

print(response)