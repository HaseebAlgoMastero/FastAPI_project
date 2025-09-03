
# main.py

from Chatbot.chatbot import Chatbot

chatbot  = Chatbot()

def main(query):
    output = chatbot.chatbot(query)
    return output

# query = "what is the answer of 2+2?"
# output = main(query)
# print(output)