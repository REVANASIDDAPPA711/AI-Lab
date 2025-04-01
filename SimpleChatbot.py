#Simple Chatbot
def simple_chatbot(uset_input):
    conversations={
        "hi":"hello!How can i help you?",
        "how are you":"I am doing well.Thank you.How about you",
        "name":"I am a chatbot.You can call me Chatpy",
        "age":"I don't have an age.I am just a program",
        "bye":"Good bye!Have a great day",
        "weather":"I am sorry.I don't have real time information.You can refer to weather related websites",
        "help":"I am here to assist you.you can ask more questions,feel free to ask",
        "python":"Python is a fantastic programming language ",
        "default":"I am sorry.I can not respond to that,ask me another question",
        "what is the time now":"now"
    }
    user_input_lower=user_input.lower()
    response=conversations.get(user_input_lower,conversations["default"])
    return response
print("Hi.I am a chatpy.Your friendly assistant.")
print("You can ask the questions now.Type 'bye' to exit")
while(True):
    user_input=input("YOU:")
    if user_input.lower()=="bye":
        print("chatpy:Goodbye!Have a great day")
        break
    response=simple_chatbot(user_input)
    print("chatpy:",response)
