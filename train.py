
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("TestBot",
                input_adapter='chatterbot.input.TerminalAdapter',
                output_adapter='chatterbot.output.TerminalAdapter'
                )
conv=[
    "hi",
    "hello",
    "How are you doing?",
    "I am fine thank you.",
    "Thats good to hear",
    "Thank you.",
    "welcome"
   ]

print("Hello!")
chatbot.set_trainer(ListTrainer)
chatbot.train(conv)
while True:
    try:    
        response=chatbot.get_response(None)
        res=input("Did I answer your question correctly? Enter yes or no \n")
        if res=='yes':
            print("I'm right!! Please continue asking your questions.")
            continue
        else:
            que=input("enter the question\n")
            ans=input("enter the answer\n")
            conv.append(que)
            conv.append(ans)
            chatbot.set_trainer(ListTrainer)
            chatbot.train(conv)
            print("Thank you for the correct answer. Anything else?")
            
       
    except(KeyboardInterrupt):
        break
    
