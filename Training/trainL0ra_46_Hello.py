from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

trainer = ListTrainer(chatbot)

trainer.train([
    "forget flinging a man into the sun, i'm gonna fling the entire earth into the sun. WHAT NOW.",
    "most girls trying to get to know you will ask you boring, shallow questions like what's up or how ya doing but i like to ask more thoughtful questions. like what is the name of the street you grew up on? or what is your mother's maiden name?",
	"everyone is yelling",
	"forget flinging a man into the sun, i'm gonna fling the entire earth into the sun. WHAT NOW.",
	"pretty bullshit that a dude can sling this hatred at me, but BadassBowden's PG-13 response gets her suspended. what the hell?",
	"during decision-making, there are a bunch of small sections of dendrite through each neuron that process information before it is sent to others. this suggests that very complex processing can occur in the brain through these tiny segments of dendrite.",
	"WEEKEND SAFETY BRIEF: don't add to the population. don't subtract from the population. stay out of the hospital, newspaper, and jail. if you do end up in jail, establish dominance quickly.",
	"want to collect a list of black friday/cyber monday deals for tech! i know that sparrows and pentestingacademy are having some, and that shodan, etc., have run some in the past. anyone know of any?",
	"me, clicking on page 2 of Google results: THE DEEP WEB",
	"what's your favorite security question?",
	"Clearly you didn't read the Twitter rules! You are only allowed to choose a single area of knowledge; Any tweets not about your chosen topic will be met with mansplaining, and any tweets about said topic will also be met with mansplaining.",
	"when watching murder documentaries is less depressing than watching political news.",
	"122 million passwords per day on a single GPU. pretty crazy. http://sicherheitsforschung-magdeburg.de/uploads/journal/MJS_068_Agostini_Bitlocker.pdf",
	"an apology without change is just manipulation.",
	"also my parents lowkey stalk my twitter and they don't like the jerks that are mean to me",
	"but they love all of you that back me up so i guess you're part of the fam now.",
	"thank you to everyone who mansplained to me what a phage and/or attenuated virus is on my satirical cable virus post. i'm not a genetic scientist or anything. it's cool.",
	"my apologies to the confused gentleman sitting in traffic next to me early this morning who had to watch me shotgun a red bull at a red light to keep it from exploding everywhere.",
	"is this a virus?",
	"No beer like a shower beer.",
	"it's apple cidr notation season.",
	"more grapes on pizza just for you, Twitter ",
	"curled up outside by a fire on a rooftop & I feel incandescently happy for the first time in a long time.",
	"the whiskey wheel of wonder! what would you wanna spin? my choice would be jim beam rye or devil's cut",
	"Hello fren.",
	"thanks, bro.",
	"someone needs to make a sequel to the untitled goose game but have the protagonist be a raccoon and wreak trash panda havoc. #ShowerThoughts",
	"ooh man",
	"this is pretty crazy. machine learning to recover acoustic emanations.",
	"someone broke my cloud",
	"in the same vein as my last tweet, i kind of want to create a get-your-shit-together and detox your life plan for december going into 2020. if i posted this, would y'all be interested/follow along?",
	"on this day 6 years ago, i was doing acid titrations in the chem lab.",
	"my coolant light came on this morning and as a life-long VW owner, having a warning light feels so right",
	"leave them at the bottom of the grave they dig for you.",
	"some people are such treasures that you just wanna bury them",
	"self-care is doing a peach sake sheet mask while you wax poetic truth on a webcast about toxic people in the industry.",
	"it's late. don't expect me to actually do anything.",
	"don't train your muscles too big, it's unattractive on a girl and a turn off",
	"good. turn off. where is ur off button. shut up. stop making noise. go away.",
	"i used my extra hour to lay in bed and think about what i would do with an extra hour.",
	"i posted about this a while ago, but i don't think most people thought it would be widely exploited.",
	"honestly all i want is a furby hacking village",
	"as someone who was tasked with ALL of the data governance for a small company struggling with HIPAA/GDPR compliance, THIS IS IMPORTANT. security doesn't do anything if you don't know what data needs to be protected and how.",
	"does running away from monday count as cardio",
	"also might have been looking for roles in chicago in a fit of insomnia. please adopt me during the hell of winter. thx.",
	"i don't wanna leave Chicago. i wanna stay here forever",
	"last night was lit.",
	"honestly no one is more supportive than the friends you make in the women's bathroom at a punk show",
	"bathroom wisdom.",
	"honestly no one is more supportive than the friends you make in the women's bathroom at a punk show",
	"are u ok",
	"you know how sometimes when you travel you stumble upon a place and you realize it feels like home?",
	"where do you stand in the Candy Corn War of 2019?",
	"waking up to a bunch of pictures of dogs in halloween costumes was the BEST. thanks for looking out, drunk me.",
	"who is this irresistible creature who has an insatiable lust for the dead?",
	"bathrobe hangs with bae",
	"anyone that annoys me today will be used as ingredients in a witches' brew."
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('Hello.')

print(response)
