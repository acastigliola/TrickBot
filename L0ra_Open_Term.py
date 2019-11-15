###################################################################
###################################################################
##   TrickBot v1.0 Chat Terminal (L0ra)                          ##
##                                                               ##
##  Written by Angelo Castigliola III                            ##
##                                                               ##
## The following python program is a simple program that runs    ##
## on the ChatterBot framework.  This program will open a        ##
## terminal to the ChatterBot named L0ra.                        ##
##                                                               ##
###################################################################
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

print('Type something to begin...')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break