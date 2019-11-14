from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

trainer = ListTrainer(chatbot)

trainer.train([
    "I'm doing well how are you?",
    "Bored, what are you up to?",
	"I was bored but I'm talking to you now :)"
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('How are you?')

print(response)