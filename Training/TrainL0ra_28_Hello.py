from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

trainer = ListTrainer(chatbot)

trainer.train([
    "Not a lot.",
    "Chilling.... lol..",
	"How are you?",
	"Nothing.",
	"Oh, just the usual.",
	"Oh gosh, all kinds of stuff!",
	"Like you, but better.",
	"I could really go for a massage.",
	"Much better now that you are with me.",
	"Not so well",
	"So far, so good!",
	"I'm pretty standard right now.",
	"Happy and content, thank you.",
	"Going great. Hope this status quo persists for rest of the day.",
	"Well enough to chat with you if you wish to.",
	"Im better than I was, but not nearly as good as I’m going to be.",
	"I think I’m doing OK. How do you think I’m doing?",
	"I am blessed!",
	"Way better than I deserve!",
	"I have a pulse, so I must be okay.",
	"Better than some, not as good as others.",
	"I'm doing really well.",
	"Medium well.",
	"I would be lying if I said I’m fine.",
	"Surviving, I guess.",
	"In need of some peace and quiet.",
	"Horrible, now that I’ve met you.",
	"Imagining myself having a fabulous vacation.",
	"I'm better on the inside than I look on the outside",
	"Sunshine all day long!",
	"I'm not sure yet.",
	"I am high-quality.",
	"Real terrible, thanks for asking.",
	"Incredibly good looking.",
	"The best I can be. Assuming you’re at your best too.",
	"I'm still sucking air.",
	"Better than nothing.",
	"I'm vertical and breathing.",
	"Different day, same existence."
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('Hello?')

print(response)
