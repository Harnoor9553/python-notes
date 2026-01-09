print("Namaste! Welcome to Your Buddy Chatbot")
print("You can ask me basic question, Type 'bye' to exit from the bot")

#Chatbot Memory Creation [dictionary of responses]
responses= {
    "hello":"Hi, welcome. How can I help you?",
    "how are you":"I am fine. Thank you",
    "who are you":"I am smart AI chatbot",
    "motivate me":"Keep going. Every bug of your project make you a better coder",
    "happy":"I'm Glad you are.",
    "Functions":"go to chp 7 see"
}
#Method/Function to get response of ChatBot
def getResponseOfBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responses:#from dictionary
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I am not able tell that yet. I am still learning."

while True:
    # take user i/p
    userInput = input("Please ask your question: ")
    reply = getResponseOfBot(userInput)
    print("Bot response:", reply)

    if "bye" in userInput.lower():
        print("Bot response: Goodbye! 👋")
        break

