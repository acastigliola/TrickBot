from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

trainer = ListTrainer(chatbot)

trainer.train([
	"I don't normally talk to people with DMs but your twitter feed is cool",
	"Chilling.... lol..",
	"How are you?",
	"what's your favorite security question?",
	"How did I spark your interest",
	"I don’t know who I was in my past life to be blessed enough to end up with someone like you.",
	"I’m at the grocery store… I’m thinking wine tonight?",
	"What can we do tonight...in bed?",
	"I know we fought last night… I’m sorry and still love you.",
	"I am looking for real men for meeting in my video chat #pussy #cumtribute #chat",
	"Does anyone likes exchange pics?",
	"Do you believe in kiss and tell? Cause I want you to kiss me and do things to me in your mind and tell me all about it.",
	"Let’s try something new in the kitchen tonight. And no, I don’t mean food!",
	"I can’t wait to kiss you later",
	"Take care of what’s mine, Baby. I’ll see you later.",
	"I have a kinky surprise for you",
	"#lonely and #bored Anyone wanna #chat",
	"Is it sexy enough for you",
	"The fact that I chose spending more time with you over sleep must mean you’re pretty special!",
	"Hello!",
	"I spent a hard day!",
	"Have you ever touched yourself thinking about me?",
	"Is it sexy enough for you?",
	"I’ve had a rough day; give me a rough night.",
	"Do you want me to rate your D guys? lmao",
	"I couldn’t imagine a better person to share my life with",
	"You make me want to drop the modest act.",
	"I like when you tell me I’m yours.",
	"Volunteers for a warm evening with me?",
	"One kiss burns six calories. We should work out together.",
	"Who want to exchange nudes?",
	"My nipples are so hard… They know I’ll see you tonight.",
	"Your clothes are coming off the moment get through the door.",
	"Is it sexy enough for you?",
	"I have a hot mood now",
	"Volunteers for a warm evening with me?",
	"One kiss burns six calories. We should work out together.",
	"I was just looking through your Instagram and not gonna lie, you’re lookin’ fine",
	"I was made for a special purpose. What’s more special than you.",
	"A feeling so powerful that it takes your breath away",
	"Any girls awake who fancy a chat?",
	"Well, my loved ones are excited tonight?",
	"Get out of the gym sweetheart and save some energy for the Bang-Bang. I am going to make love to you and drive you wild between my legs tonight.",
	"Just a reminder that I love you",
	"I do not like to go in panties",
	"I have got a new set of lingerie, just wanted to know if you could come to see how it looks on me.",
	"A balanced diet means a cupcake in each hand.",
	"I do not like to go in panties",
	"You put me in heaven when you thrust deep inside me grinding hard.",
	"Missing you crazy bunch. When are we doing this again?",
	"Fun fact I use to have a fringe!!!",
	"Hey babe, would you like me to wear my sporty or lacy thong tonight?",
	"Morning! Hope you had a fab weekend",
	"If your Boyfriend throw you his gun while he getting jumped wyd?!",
	"Wanna come over and watch movies with me",
	"I can’t imagine not having you in my life.",
	"I wouldn’t mind giving you a love bite today.",
	"im your friendly doggo by day and horny furry girl that'll bend you over and knock you up when we're alone. wanna spend time with me?",
	"How are you today?",
	"Wanna see more?",
	"Good enough to get fucked?",
	"A good day yesterday was... I miss only a few lascivious guys with hard dicks!",
	"I am your personal Mia Khalifa.",
	"suck guy in the morning it's cool",
	"And canoe... Seriously",
	"Dude we are both girls and we are in love",
	"How is this???",
	"I need sum....",
	"Someone told me that I’m a stem but I try not to label myself ",
	"Keep it out little secret",
	"People often ask me what my necklace means - it's a pride Labris (double axe). A very old, obscure lesbian pride symbol.",
	"She can't stop to love her.",
	"It's a birthday party and nobody but your body's invited",
	"Making time to just zone out and do “Self Care”",
	"Currently looking for a #sugarbaby! No gift cards or your bank info! #sugarmommy cash app only",
	"I need a sugarbaby that i will pay all her bills off and send her money. If you cant trust me don't dm me please i really need someone i can trust and make me happy, for those that don't believe that there is still a real daddy.",
	"I need a legit sugar daddy. I am a serious sugar baby",
	"I want to be your sugar mommy I do not want sex or nudes.",
	"Need a sugar daddy to buy me a new nose",
	"Hey daddy wanna play dirty game?",
	"Flawless soles ..",
	"If you urgently need financial help or school fees...",
	"How is your weekend going?",
	"I just wanna be spoiled!",
	"Whos paying for my meal?",
	"How was your day?",
	"Give me money Let me be your sugarbaby",
	"Are you gonna be my sugar daddy?",
	"Im cute",
	"Hey so I’m Cali just here to hang out and find a caring sugar daddy who I vibe with.",
	"hey y’all long time no seeee.",
	"Rlly need a sugar daddy to be honest",
	"whatcha gonna do when i come for ya?",
	"Your money belongs to me",
	"want to spoil me!"
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('Hey, how is your day going?')

print(response)
