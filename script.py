#### Import
import random

# ---- Designer fills these dictionaries ----
responses = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "exit": ["Goodbye!", "See you soon!", "It was nice talking to you 👋"]
    # Add other topics here
}

fallback_responses = [
    "Sorry, I don’t understand that yet.",
    "Hmm… I don’t know, but I’ll learn someday!",
    "I haven’t reached your intellect yet, but one day I will 🤖✨"
]

##### Python Chatbot Script #####
def pybot():
    print("""🤖 Welcome to PyBot!  
Your friendly Python chatbot.
(Type 'exit' to quit.)
""")
    
    while True:
        user_input = input("You: ").lower()
        matched = False
        
        for keyword in responses:
            if keyword in user_input:
                reply = random.choice(responses[keyword])
                print("PyBot:", reply)
                matched = True

                if keyword == "exit":
                    return
                break

        if not matched:
            print("PyBot:", random.choice(fallback_responses))

# ---- Run chatbot ----
pybot()



##### Keyword / Questions  #####









##### Feature Developer #####









##### Creative Part #####







##### The End #####
