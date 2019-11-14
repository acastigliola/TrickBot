from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

trainer = ListTrainer(chatbot)

trainer.train([
    "I don't normally talk to people with DMs but your twitter feed is cool",
    "Chilling.... lol..",
	"How are you?"
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('Hi')

print(response)