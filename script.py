##### Python Chatbot Script #####








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

def get_chatbot_info(query):
        about_chatbot = {"name": "pybot",
                        "creator": "umi_waqar_Nedim",
                        "purpose": "Assist users with various queries and provide information.",
                        "age": 10}
        if "name" in query.lower():
                        return f"My name is {about_chatbot['name']}."
        elif "creator" in query.lower():
                        return f"I was created by {about_chatbot['creator']}."
        elif "purpose" in query.lower():
                        return f"My purpose is to {about_chatbot['purpose']}."
        elif "age" in query.lower():
                        return f"I am {about_chatbot['age']} years old."
        else:
                        return "I'm not sure about that. Can you ask something else?"


#motivation and study

motivation_and_study = {"motivation1":"How can I improve myself?",
                        "motivation2":"How can I help you more efficiently?",
                        "motivation3":"Is the world spherical or flat?",
                        "motivation4":"What is the weight of each single continent of Earth?"}

#weather
cities_weather = {"Berlin":["sunny 20°", "rainy 10°", "cloudy 5°", "windy 7°", "snowy 1°"],
"Paris": ["sunny 20°", "rainy 13°", "cloudy 5°", "windy 10°", "snowy 1°"],
"Rome":["sunny 21°", "rainy", "cloudy", "windy", "snowy 1°"],
"Barcelona":["sunny 22°", "rainy 15°", "cloudy 18°", "windy 15°", "snowy 1°"],
"Berlin":["sunny 20°", "rainy", "cloudy", "windy", "snowy 1°"]}

#random facts
random_facts_2 = {"fact1": "Wombat poop is cube-shaped.",
                "fact2": "A day on Venus is longer than a year on Venus.",
                "fact3": "Humans share 60% of their DNA with bananas.",
                "fact4": "The Eiffel Tower can be 15 cm taller during the summer."}

food = {"breakfast":["Oatmeal with Fruits: Warm oatmeal topped with sliced bananas and berries.",
                     "Scrambled Eggs: Fluffy scrambled eggs served with whole-grain toast."],
        "lunch":["Caprese Salad: Fresh mozzarella, tomatoes, and basil drizzled with balsamic glaze.",
                "Turkey Sandwich: Sliced turkey, lettuce, and tomato on whole grain bread."],
        "dinner":["Grilled Chicken with Veggies: Marinated grilled chicken served with steamed vegetables.",
                "Spaghetti Aglio e Olio: Spaghetti tossed with garlic, olive oil, and chili flakes."]}

#Exit goodbye

goodbye_greetings = {"goodbye": "Goodbye! It was great chatting with you. Have a wonderful day!",
                    "bye": "See you later! Don't be a stranger!",
                    "bye bye": "Take care! Looking forward to our next conversation!",
                    "farewell": "Farewell! Wishing you all the best until we chat again!"}