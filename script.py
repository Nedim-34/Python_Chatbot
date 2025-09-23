import tkinter as tk
from tkinter import scrolledtext
import random
import pytz
import datetime
import re
import operator

# ---- Chatbot Logic code ----
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
    "motivation, motivate tip":["Never give up and keep work hard?"],
    "study help":["Create a dedicated study schedule to manage your time effectively.", "Use active learning techniques, such as summarizing information or teaching it to someone else.", "Take regular breaks to maintain focus and avoid burnout."],
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


# ---- chatbot logic (modified for GUI) ----
class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("PyBot Chatbot")
        master.geometry("500x600")

        self.user_memory = {}
        self.topic_dicts = [
            responses, greetings, about_chatbot, motivation_and_study,
            cities_weather, food, goodbye_greetings, timezones, fallback_responses
        ]

        # Chat window
        self.chat_window = scrolledtext.ScrolledText(master, state='disabled', wrap='word')
        self.chat_window.pack(padx=10, pady=10, fill='both', expand=True)
        self.chat_window.tag_configure('user', foreground='white')
        self.chat_window.tag_configure('bot', foreground='cyan')

        # Input box and send button
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(padx=10, pady=(0, 10), fill='x')

        self.input_box = tk.Entry(self.input_frame)
        self.input_box.pack(side='left', fill='x', expand=True, padx=(0, 5))
        self.input_box.bind("<Return>", self.process_user_input)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.process_user_input)
        self.send_button.pack(side='right')

        # Initial message
        self.display_message("PyBot: Hello, I'm PyBot! How can I help you? 👋", 'bot')

    def display_message(self, message, sender):
        """Displays a message in the chat window."""
        self.chat_window.config(state='normal')
        self.chat_window.insert(tk.END, message + "\n\n", sender)
        self.chat_window.config(state='disabled')
        self.chat_window.yview(tk.END)

    def process_user_input(self, event=None):
        """Handles user input and generates a bot response."""
        user_input = self.input_box.get()
        if not user_input.strip():
            return

        self.display_message(f"You: {user_input}", 'user')
        self.input_box.delete(0, tk.END)
        self.master.after(500, lambda: self.generate_bot_response(user_input))

    def generate_bot_response(self, user_input):
        """Generates a response from the chatbot logic."""
        user_input_lower = user_input.lower()
        response = None

        # Check for memory retrieval
        if "what is my name" in user_input_lower:
            if "name" in self.user_memory:
                response = f"Your name is {self.user_memory['name'].capitalize()}"
            else:
                response = "I don't know your name yet. You can tell me by saying 'my name is [your name]'."

        # Check for name setting
        if not response and "my name is" in user_input_lower:
            match = re.search(r'my name is (.+)', user_input_lower)
            if match:
                name = match.group(1).strip()
                self.user_memory['name'] = name
                response = f"Hello, {name.capitalize()}! I'll remember that."

        # Check for math calculation
        if not response and any(op in user_input_lower for op in ['+', '-', '*', '/', '^']):
            result, error = calculate(user_input_lower)
            response = result if result else error

        # Check for time-related queries
        if not response:
            time_match = re.search(r'time in ([\w\s]+)', user_input_lower)
            if time_match:
                city = time_match.group(1).strip()
                response = get_time(city)

        # Check jokes and random facts
        if not response:
            if "joke" in user_input_lower:
                response = random.choice(jokes)
            elif "fact" in user_input_lower:
                response = random.choice(random_facts)

        # Check general topics
        if not response:
            for topic in self.topic_dicts:
                for key in topic:
                    if key in user_input_lower:
                        if key in motivation_and_study:
                            response = topic[key]
                        else:
                            response = random.choice(topic[key])
                        break
                if response:
                    break

        # Fallback response if no match is found
        if not response:
            response = random.choice(fallback_responses)

        # Display the final response
        if isinstance(response, list):  # Handle list responses like 'study help'
            for item in response:
                self.display_message(f"PyBot: {item}", 'bot')
        else:
            self.display_message(f"PyBot: {response}", 'bot')

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()



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
