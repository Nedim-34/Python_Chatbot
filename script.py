#### Import
import random
import pytz
import datetime
import re
import operator

# ---- Designer fills these dictionaries ----
responses = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "exit": ["Goodbye!", "See you soon!", "It was nice talking to you 👋"]
}
greetings = {
    "hello": ["Hi there! How can I help you today?"],
    "hi": ["Hello! What can I do for you?"],
    "hey": ["Hey! How's it going?"],
    "good morning": ["Good morning! Hope you have a great day ahead!"],
    "good afternoon": ["Good afternoon! How can I help you?"],
    "good evening": ["Good evening! What would you like to know?"],
    "bye": ["Goodbye! Have a wonderful day!"],
    "thanks": ["You're welcome! If you need anything else, just ask."]
}

# Combined jokes into a single list for random choice
jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my computer I needed a break, and now it won’t stop sending me beach wallpapers.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the bicycle fall over? It was two-tired!",
    "What do you call a Mexican who has lost his car? Carlos",
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a fake noodle? An Impasta!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]

# Combined random facts into a single list
random_facts = [
    "Wombat poop is cube-shaped.",
    "A day on Venus is longer than a year on Venus.",
    "Humans share 60% of their DNA with bananas.",
    "The Eiffel Tower can be 15 cm taller during the summer."
]

about_chatbot = {
    "name": ["Pybot"],
    "creator": ["Umi Waqar Nedim"],
    "purpose": ["Assist users with various queries and provide information."],
    "age": ["5 days but still growing"],
    "about you": ["My name is PyBot and was created by Umi Waqar Nedim, I Assist users with various queries and provide information and i´m still 5 days old but still growing"] 
}

motivation_and_study = {
    #"how can i improve myself?": "By setting clear goals, learning new skills, and seeking feedback.",
    #"how can i help you more efficiently?": "You can provide clear and specific questions.",
    #"is the world spherical or flat?": "The Earth is an oblate spheroid, which is a slightly flattened sphere.",
    #"what is the weight of each single continent of earth?": "Continents don't have a single, measurable weight. They are part of the Earth's crust."
    "motivation motivate tip":["Never give up and keep work hard?"],
    "study help":["Create a dedicated study schedule to manage your time effectively.",
                "Use active learning techniques, such as summarizing information or teaching it to someone else.",
                "Take regular breaks to maintain focus and avoid burnout."],
    "focus focusing meditation":["take a deep breathe, and focus on your goals",
                "Practice deep breathing for a few minutes to center your mind.",
                "Set a timer for short meditation sessions to build consistency."]
}

cities_weather = {
    "weather in berlin":["It is sunny, 20°C", "It is rainy, 10°C", "It is cloudy, 5°C", "It is windy 7°C", "It is snowy 0°C"],
    "weather in paris":["It is sunny, 20°C", "It is rainy, 10°C", "It is cloudy, 5°C", "It is windy 7°C", "It is snowy 0°C"],
    "weather in rome":["It is sunny, 20°C", "It is rainy, 10°C", "It is cloudy, 5°C", "It is windy 7°C", "It is snowy 0°C"],
    "weather in barcelona":["It is sunny, 20°C", "It is rainy, 10°C", "It is cloudy, 5°C", "It is windy 7°C", "It is snowy 0°C"],
    "weather in london":["It is sunny, 20°C", "It is rainy, 10°C", "It is cloudy, 5°C", "It is windy 7°C", "It is snowy 0°C"]
}

food = {
    "breakfast": ["Oatmeal with Fruits: Warm oatmeal topped with sliced bananas and berries.", 
                  "Scrambled Eggs: Fluffy scrambled eggs served with whole-grain toast."],
    "lunch": ["Caprese Salad: Fresh mozzarella, tomatoes, and basil drizzled with balsamic glaze.", 
              "Turkey Sandwich: Sliced turkey, lettuce, and tomato on whole grain bread."],
    "dinner": ["Grilled Chicken with Veggies: Marinated grilled chicken served with steamed vegetables.", 
               "Spaghetti Aglio e Olio: Spaghetti tossed with garlic, olive oil, and chili flakes."]}

goodbye_greetings = {
    "goodbye": ["Goodbye! It was great chatting with you. Have a wonderful day!","See you later! Don't be a stranger!","Take care! Looking forward to our next conversation!","Farewell! Wishing you all the best until we chat again!"],
    "bye":["Goodbye! It was great chatting with you. Have a wonderful day!","See you later! Don't be a stranger!","Take care! Looking forward to our next conversation!","Farewell! Wishing you all the best until we chat again!"],
    "bye bye":["Goodbye! It was great chatting with you. Have a wonderful day!","See you later! Don't be a stranger!","Take care! Looking forward to our next conversation!","Farewell! Wishing you all the best until we chat again!"],
    "farewell":["Goodbye! It was great chatting with you. Have a wonderful day!","See you later! Don't be a stranger!","Take care! Looking forward to our next conversation!","Farewell! Wishing you all the best until we chat again!"]
}

fallback_responses = [
    "Sorry, I don’t understand that yet.",
    "Hmm… I don’t know, but I’ll learn someday!",
    "I haven’t reached your intellect yet, but one day I will 🤖✨"
    "That’s an interesting thought! Could you elaborate a bit more?",
    "That seems a bit unclear. Can you provide more details?",
    "I’m here to help, but I need a bit more context. What do you mean?"
]

motivation_and_study = {"motivation motivate tip":["Never give up and keep work hard?"],
                        "study help":["Create a dedicated study schedule to manage your time effectively.",
                                    "Use active learning techniques, such as summarizing information or teaching it to someone else.",
                                    "Take regular breaks to maintain focus and avoid burnout."],
                        "focus focusing meditation":["take a deep breathe,  and focus on your goals",
                                                      "Practice deep breathing for a few minutes to center your mind.",
                                                              "Set a timer for short meditation sessions to build consistency."]}

cities_weather = {"berlin weather":["It is sunny, 20°C", "It is rainy, 10°C", "It is cloudy, 5°C", "It is windy 7°C", "It is snowy 0°C"],
"paris weather":["It is sunny, 20°C", "It is rainy, 10°C", "It is cloudy, 5°C", "It is windy 7°C", "It is snowy 0°C"],
"rome weather":["It is sunny, 20°C", "It is rainy, 10°C", "It is cloudy, 5°C", "It is windy 7°C", "It is snowy 0°C"],
"barcelona weather":["It is sunny, 20°C", "It is rainy, 10°C", "It is cloudy, 5°C", "It is windy 7°C", "It is snowy 0°C"],
"london weather":["It is sunny, 20°C", "It is rainy, 10°C", "It is cloudy, 5°C", "It is windy 7°C", "It is snowy 0°C"]}



food = {"breakfast":["Oatmeal with Fruits: Warm oatmeal topped with sliced bananas and berries.",
                     "Scrambled Eggs: Fluffy scrambled eggs served with whole-grain toast."],
        "lunch":["Caprese Salad: Fresh mozzarella, tomatoes, and basil drizzled with balsamic glaze.",
                "Turkey Sandwich: Sliced turkey, lettuce, and tomato on whole grain bread."],
        "dinner":["Grilled Chicken with Veggies: Marinated grilled chicken served with steamed vegetables.",
                "Spaghetti Aglio e Olio: Spaghetti tossed with garlic, olive oil, and chili flakes."]}

goodbye_greetings = {"goodbye": ["Goodbye! It was great chatting with you. Have a wonderful day!","See you later! Don't be a stranger!","Take care! Looking forward to our next conversation!","Farewell! Wishing you all the best until we chat again!"],
                    "bye":["Goodbye! It was great chatting with you. Have a wonderful day!","See you later! Don't be a stranger!","Take care! Looking forward to our next conversation!","Farewell! Wishing you all the best until we chat again!"],
                    "bye bye":["Goodbye! It was great chatting with you. Have a wonderful day!","See you later! Don't be a stranger!","Take care! Looking forward to our next conversation!","Farewell! Wishing you all the best until we chat again!"],
                    "farewell":["Goodbye! It was great chatting with you. Have a wonderful day!","See you later! Don't be a stranger!","Take care! Looking forward to our next conversation!","Farewell! Wishing you all the best until we chat again!"]}

fallback_responses = [ "That’s an interesting thought! Could you elaborate a bit more?",
    "That seems a bit unclear. Can you provide more details?",
    "I’m here to help, but I need a bit more context. What do you mean?"]


timezones = {
    "new york": "America/New_York",
    "london": "Europe/London",
    "tokyo": "Asia/Tokyo",
    "sydney": "Australia/Sydney",
    "mumbai": "Asia/Kolkata",
    "dubai": "Asia/Dubai",
    "moscow": "Europe/Moscow",
    "berlin": "Europe/Berlin",
    "istanbul": "Asia/Istanbul",
    "nairobi": "Africa/Nairobi"
}

# Dictionary mapping string operators to functions
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

def calculate(expression):
    """Safely evaluates a simple mathematical expression."""
    match = re.search(r'(-?\d+\.?\d*)\s*([+\-*/^])\s*(-?\d+\.?\d*)', expression)
    if not match:
        return None, "I can only handle simple calculations like '2 + 2' or '5 * 8'."
    
    try:
        num1 = float(match.group(1))
        op = match.group(2)
        num2 = float(match.group(3))
        
        func = OPERATORS.get(op)
        if func:
            result = func(num1, num2)
            return f"The answer is {result}.", None
        else:
            return None, "Sorry, I can't perform that operation."
    except (ValueError, ZeroDivisionError) as e:
        return None, f"An error occurred during calculation: {e}"


def get_time(city):
    """Provides the time for a specified city or location."""
    tz = timezones.get(city)
    if tz:
        try:
            city_tz = pytz.timezone(tz)
            city_time = datetime.datetime.now(city_tz).strftime("%I:%M %p on %A, %B %d")
            return f"The current time in {city.capitalize()} is {city_time}."
        except pytz.UnknownTimeZoneError:
            return "Sorry, I couldn't find that time zone."
    return "I can tell you the time in New York, London, Tokyo, Sydney, Mumbai, Dubai, Moscow, Berlin, or Istanbul."


# ---- chatbot loop ----
topic_dicts = [
    responses, greetings, about_chatbot, motivation_and_study,
    cities_weather, food, goodbye_greetings, timezones
]

##### Python Chatbot Script #####
def pybot():
    print("""\n🤖 Welcome to PyBot!  
Your friendly Python chatbot.
\n(Type 'exit' to quit.)
""")

    user_memory = {}
    first_interaction = True
    
    while True:
        if first_interaction:
            print("PyBot: Hello, I'm PyBot! How can I help you?")
            first_interaction = False
        
        user_input = input("You: ").lower()
        matched = False

        # Check for memory retrieval first
        if not matched and "what is my name" in user_input:
            if "name" in user_memory:
                print(f"PyBot: Your name is {user_memory['name'].capitalize()}")
            else:
                print("PyBot: I don't know your name yet. You can tell me by saying 'my name is [your name]'.")
            matched = True

        if not matched and "my name is" in user_input:
            match = re.search(r'my name is (.+)', user_input)
            if match:
                name = match.group(1).strip()
                user_memory['name'] = name
                print(f"PyBot: Hello, {name.capitalize()}! I'll remember that.\n")
            matched = True

        # Check for math calculation
        if not matched and any(op in user_input for op in ['+', '-', '*', '/', '^']):
            result, error = calculate(user_input)
            if result:
                print("PyBot:", result)
            else:
                print("PyBot:", error)
            matched = True
        
        if not matched:
            # Check for time-related queries
            time_match = re.search(r'time in ([\w\s]+)', user_input)
            if time_match:
                city = time_match.group(1).strip()
                print("PyBot:", get_time(city))
                matched = True
        
        # Check jokes and random facts
        if not matched:
            if "joke" in user_input:
                print("PyBot:", random.choice(jokes))
                matched = True
            elif "fact" in user_input:
                print("PyBot:", random.choice(random_facts))
                matched = True

        if not matched:
            for topic in topic_dicts:
                for key in topic:
                    if key in user_input:
                        if key in motivation_and_study:
                            reply = topic[key]
                        else:
                            reply = random.choice(topic[key])
                        print("PyBot:", reply)
                        matched = True
                        break
                if matched:
                    break

        # Fallback response if no match is found
        if not matched:
            print("PyBot:", random.choice(fallback_responses))

# ---- Run chatbot ----
pybot()



##### Keyword / Questions  #####









##### Feature Developer #####









##### Creative Part #####




# #show current date
# from datetime import datetime
# date_time = {"current_date": datetime.now().strftime('%Y-%m-%d'),
#             "current_time": datetime.now().strftime('%H:%M:%S')}
# print(date_time)

# #math helper

# def add(num1, num2):
#         return num1 + num2
# def subtract(num1, num2):
#         return num1 - num2
# def multiply(num1, num2):
#         return num1 * num2
# def divide(num1, num2):
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "incorrect input,division by 0 isn't allowed."
        
# math_helper = {"add": add,
#                 "subtract": subtract,
#                 "multiply": multiply,
#                 "divide": divide}
# if __name__ == "__main__":
#         test_add = math_helper['add'](1, 1)
#         test_subtract = math_helper['subtract'](2,1)
#         test_multiply = math_helper['multiply'](2, 2)
#         test_divide = math_helper['divide'](7, 0)
#         print(f"Addition: {test_add}")
#         print(f"Subtraction: {test_subtract}")
#         print(f"Multiplication: {test_multiply}")
#         print(f"Division: {test_divide}")

# #memory
# memory = {"username": "",
#         "what_is_your_name": "What is your name?",
#         "how_can_i_help_you_today": "How can I help you today?"}
