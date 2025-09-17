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

greeting = {"hello": "Hi there! How can I help you today?",
            "hi": "Hello! What can I do for you?",
            "hey": "Hey! How's it going?",
            "good morning": "Good morning! Hope you have a great day ahead!",
            "good afternoon": "Good afternoon! How can I help you?",
            "good evening": "Good evening! What would you like to know?",
            "bye": "Goodbye! Have a wonderful day!",
            "thanks": "You're welcome! If you need anything else, just ask."}

#show current date
from datetime import datetime
date_time = {"current_date": datetime.now().strftime('%Y-%m-%d'),
            "current_time": datetime.now().strftime('%H:%M:%S')}
print(date_time)

#math helper

def add(num1, num2):
        return num1 + num2
def subtract(num1, num2):
        return num1 - num2
def multiply(num1, num2):
        return num1 * num2
def divide(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "incorrect input,division by 0 isn't allowed."
        
math_helper = {"add": add,
                "subtract": subtract,
                "multiply": multiply,
                "divide": divide}
if __name__ == "__main__":
        test_add = math_helper['add'](1, 1)
        test_subtract = math_helper['subtract'](2,1)
        test_multiply = math_helper['multiply'](2, 2)
        test_divide = math_helper['divide'](7, 0)
        print(f"Addition: {test_add}")
        print(f"Subtraction: {test_subtract}")
        print(f"Multiplication: {test_multiply}")
        print(f"Division: {test_divide}")

#jokes

jokes = {"joke1": "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "joke2": "I told my computer I needed a break, and now it won’t stop sending me beach wallpapers.",
        "joke3": "Why don’t skeletons fight each other? They don’t have the guts.",
        "joke4": "What do you call fake spaghetti? An impasta!",
        "joke5": "Why did the bicycle fall over? It was two-tired!",
        "joke7": "what do you call a mexican who has lost his car? Carlos"}
#test_library_joke
joke_number_7 = jokes["joke7"]
print(joke_number_7)

#about chatbot

about_chatbot = {"name": "pybot",
                "creator": "umi_waqar_Nedim",
                "purpose": "Assist users with various queries and provide information.",
                "age": 10}
#motivation and study
motivation_and_study = {"How can I improve myself?",
"How can I help you more efficiently?",
"Is the world spherical or flat?",
"What is the weight of each single continent of Earth?"}

#weather
cities_weather = {"Berlin":["sunny", "rainy", "cloudy", "windy", "snowy"],
"Paris": ["sunny", "rainy", "cloudy", "windy", "snowy"],
"Rome":["sunny", "rainy", "cloudy", "windy", "snowy"],
"Prague":["sunny", "rainy", "cloudy", "windy", "snowy"],
"Sofia":["sunny", "rainy", "cloudy", "windy", "snowy"]}

#random facts
random_facts_2 = {"fact1": "Wombat poop is cube-shaped.",
                "fact2": "A day on Venus is longer than a year on Venus.",
                "fact3": "Humans share 60% of their DNA with bananas.",
                "fact4": "The Eiffel Tower can be 15 cm taller during the summer."}

#memory
memory = {"username": "",
        "what_is_your_name": "What is your name?",
        "how_can_i_help_you_today": "How can I help you today?"}
#food
food = {"breakfast":["Oatmeal with Fruits: Warm oatmeal topped with sliced bananas and berries.",
                     "Scrambled Eggs: Fluffy scrambled eggs served with whole-grain toast."],
        "lunch":["Caprese Salad: Fresh mozzarella, tomatoes, and basil drizzled with balsamic glaze.",
                "Turkey Sandwich: Sliced turkey, lettuce, and tomato on whole grain bread."],
        "dinner":["Grilled Chicken with Veggies: Marinated grilled chicken served with steamed vegetables.",
                "Spaghetti Aglio e Olio: Spaghetti tossed with garlic, olive oil, and chili flakes."]}

#Exit goodbye

goodbye_greetings = {"greeting1": "Goodbye! It was great chatting with you. Have a wonderful day!",
                    "greeting2": "See you later! Don't be a stranger!",
                    "greeting3": "Take care! Looking forward to our next conversation!",
                    "greeting4": "Farewell! Wishing you all the best until we chat again!"}