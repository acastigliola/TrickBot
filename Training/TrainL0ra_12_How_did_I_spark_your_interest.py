from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

trainer = ListTrainer(chatbot)

trainer.train([
    "You have a really cool twitter feed. Do you hack?",
	"You seem cool. I like your feed.",
	"You seem intresting.",
	"I think I like you.",
	"Because you are intresting. Good? :)"
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('How did I spark your interest?')

print(response)