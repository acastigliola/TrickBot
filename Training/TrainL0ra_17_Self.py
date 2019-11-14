from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

trainer = ListTrainer(chatbot)

trainer.train([
    "Caffeine free tea and honey... warm.",
	"Just handing out talking to you.",
	"Just talking to you :)"
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('Self?')

print(response)