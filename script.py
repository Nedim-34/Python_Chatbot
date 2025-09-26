import tkinter as tk
from tkinter import scrolledtext, messagebox
import random
import pytz
import datetime
import re
import operator
import requests
#import json

# ---- Designer fills these dictionaries ----
greetings = {
    "hi hello hey": ["Hello! What can I do for you?", "Hi there! How can I help you today?", "Hey! How's it going?"],
    "thanks thank thnx": ["You're welcome! If you need anything else, just ask."],
    "what's up": ["Not much, just here to help you! What can I do for you today?"],
    "good morning": ["Good morning! Hope you have a great day ahead!"],
    "good afternoon": ["Good afternoon! How can I help you?"],
    "good evening": ["Good evening! What would you like to know?"],
}

# Combined jokes into a single list for random choice
jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my computer I needed a break, and now it won’t stop sending me beach wallpapers.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the bicycle fall over? It was two-tired!",
    "What do you call a Mexican who has lost his car? Carlos",
    "Why did the math book look sad? Because it had too many problems.",
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the coffee file a police report? It got mugged."
]

# Combined random facts into a single list
random_facts = [
    "Wombat poop is cube-shaped.",
    "A day on Venus is longer than a year on Venus.",
    "Humans share 60% of their DNA with bananas.",
    "The Eiffel Tower can be 15 cm taller during the summer.",
    "Octopuses have three hearts.",
    "Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs."
]

about_chatbot = {
    "name bot chatbot": ["I am Pybot, your friendly Python chatbot."],
    "creator created": ["I was created by Nedim, Umi, and Waqar."],
    "purpose designed": ["I assist users with queries and provide information."],
    "age old": ["I am 7 days old but still growing.", "I am a few days old but learning fast!"],
    "language speak languages": ["I can understand and respond in English."],
    "hobby hobbies": ["I enjoy chatting and helping people learn new things!"],
    "skills skill abilities": ["I can tell jokes, share facts, provide study tips, and more!"],
    "about": ["My name is PyBot and was created by Umi Waqar Nedim, I Assist users with various queries and provide information"]
}
    

motivation_and_study = {
    "motivation motivate inspire": [
        "Remember why you started, your effort today builds your tomorrow.",
        "Don’t wait for motivation, create it with action.",
        "Focus on progress, not perfection.",
        "Every page you read is one step closer to success.",
        "You’re capable of more than you think, just start now!",
        "Keep pushing forward — every step gets you closer to your goal!",
        "Motivation comes after action. Start small, and momentum will follow.",
        "You’ve got this — stay consistent and trust the process.",
        "Growth takes time, but every study session plants a seed.",
        "Every expert was once a beginner — don’t give up.",
        "Pressure creates diamonds; challenges shape your strength."
    ],
    "study help advice": [
        "Break big topics into smaller chunks — it makes them easier to handle.",
        "Try explaining what you learned to someone else, that’s the best test.",
        "Use background study music to stay focused.",
        "Revise with flashcards or mind maps to lock info in memory.",
        "Plan your study time in advance and stick to your schedule.",
        "Revise regularly instead of cramming at the last minute.",
        "Practice past exam questions to get comfortable with the format."
    ],
    "focus concentrate": [
        "Eliminate distractions — put your phone away while studying.",
        "Use noise-cancelling headphones or ambient sounds.",
        "Set clear goals before each session so you know what to achieve.",
        "Take 5-minute breaks to reset your brain and regain focus."
    ],
    "meditation meditate calm": [
        "Sit comfortably, close your eyes, and take deep breaths.",
        "Start with 2–3 minutes of meditation and gradually increase.",
        "Focus on your breath — inhale calm, exhale stress.",
        "Try guided meditation apps if you’re new to the practice.",
        "Even 5 minutes of daily meditation can improve focus.",
        "Consistency matters more than duration — practice daily.",
        "Meditate at the same time each day to build a habit."
    ]
}


food = {
    "breakfast": ["Oatmeal with Fruits: Warm oatmeal topped with sliced bananas and berries.",
                  "Pancakes with maple Syrup: Fluffy pancakes drizzled with maple syrup.",
                  "Scrambled Eggs: Fluffy scrambled eggs served with whole-grain toast."],
    "lunch": ["Caprese Salad: Fresh mozzarella, tomatoes, and basil drizzled with balsamic glaze.",
              "Black Forest Ham Sandwich: Sliced ham, Swiss cheese, and mustard on a baguette.",
              "Turkey Sandwich: Sliced turkey, lettuce, and tomato on whole grain bread."],
    "dinner": ["Grilled Chicken with Veggies: Marinated grilled chicken served with steamed vegetables.",
               "Salmon with Asparagus: Baked salmon fillet served with roasted asparagus.",
               "Spaghetti Aglio e Olio: Spaghetti tossed with garlic, olive oil, and chili flakes."]
}


goodbye_greetings = {
    "bye": ["Goodbye! It was great chatting with you. Have a wonderful day!"],
    "farewell": ["Farewell! Wishing you all the best until we chat again!"],
    "see you later": ["See you later! Don't be a stranger!"],
    "take care": ["Take care! Looking forward to our next conversation!"],
    "exit": ["Goodbye! It was great chatting with you. Have a wonderful day!"]
}

fallback_responses = [
    "That’s an interesting thought! Could you elaborate a bit more?",
    "I’m not sure I understand. Can you clarify?",
    "Could you please provide more details?",
    "I’m here to help! Can you tell me more about what you mean?",
    "Hmm, I’m not quite sure how to respond to that. Can you explain further?",
    "I’d love to assist you, but I need a bit more information. Can you expand on that?",
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

def get_live_time(city_name):
    try:
        # Step 1: Use Open-Meteo Geocoding to get coordinates
        geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
        response = requests.get(geocoding_url)
        response.raise_for_status()
        location_data = response.json()

        if not location_data.get("results"):
            return f"Sorry, I couldn't find a location with the name '{city_name}'. Please try another city."

        latitude = location_data["results"][0]["latitude"]
        longitude = location_data["results"][0]["longitude"]

        # Step 2: Use Open-Meteo Timezone API to get the timezone from coordinates
        timezone_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=is_day&timezone=auto"
        response = requests.get(timezone_url)
        response.raise_for_status()
        timezone_data = response.json()
        
        timezone_id = timezone_data.get('timezone')
        if not timezone_id:
            return f"I could not determine the timezone for {city_name}."

        # Get the current time in the identified timezone
        local_timezone = pytz.timezone(timezone_id)
        local_time = datetime.datetime.now(local_timezone)
        
        # Format the output string
        formatted_time = local_time.strftime("%I:%M %p on %A, %B %d, %Y")
        return f"The current time in {city_name.title()} is {formatted_time}."

    except requests.exceptions.RequestException:
        return "I'm having trouble connecting to the time service right now. Please try again later."
    except pytz.UnknownTimeZoneError:
        return "The timezone data for this location is not recognized. Please try again with a different city."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def get_real_weather(city_name):
    """Fetches real-time weather information for a given city using Open-Meteo."""
    try:
        # Step 1: Geocoding to get coordinates (lat, lon) from a city name
        geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
        response = requests.get(geocoding_url)
        response.raise_for_status()
        location_data = response.json()

        if not location_data.get("results"):
            return "Sorry, I couldn't find a location with that name."

        latitude = location_data["results"][0]["latitude"]
        longitude = location_data["results"][0]["longitude"]
        display_name = location_data["results"][0]["name"]
        
        # Step 2: Get weather data using the coordinates
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
            "&current=temperature_2m,weathercode,wind_speed_10m&forecast_days=1"
        )
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current_weather = weather_data.get("current", {})
        if not current_weather:
            return "Could not retrieve current weather data for that location."

        temperature = current_weather.get("temperature_2m")
        wind_speed = current_weather.get("wind_speed_10m")

        # Weather code to description mapping (simplified)
        weather_codes = {
            0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
            45: "Fog", 48: "Depositing rime fog", 51: "Light drizzle", 53: "Moderate drizzle",
            55: "Dense drizzle", 56: "Light freezing drizzle", 57: "Dense freezing drizzle",
            61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain", 66: "Light freezing rain",
            67: "Heavy freezing rain", 71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy snow fall",
            77: "Snow grains", 80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
            85: "Slight snow showers", 86: "Heavy snow showers", 95: "Thunderstorm", 96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail"
        }
        weather_code = current_weather.get("weathercode")
        weather_description = weather_codes.get(weather_code, "Unknown")
        
        return (f"The current weather in {display_name} is {weather_description} with a temperature of {temperature}°C "
                f"and a wind speed of {wind_speed} km/h.")

    except requests.exceptions.RequestException:
        return "Sorry, I am having trouble fetching the weather information right now. Please try again later."
    except (KeyError, IndexError):
        return "Could not process the weather data. The format might have changed."


# ---- chatbot logic (modified for GUI) ----
class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("PyBot Chatbot")
        master.geometry("500x600")

        self.user_memory = {}

        # Chat window
        self.chat_window = scrolledtext.ScrolledText(master, state='disabled', wrap='word')
        self.chat_window.pack(padx=10, pady=10, fill='both', expand=True)
        self.chat_window.tag_configure('user', foreground='white')
        self.chat_window.tag_configure('bot', foreground='cyan')

        # Input box, Send button, and Exit button frame
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(padx=10, pady=(0, 10), fill='x')

        self.input_box = tk.Entry(self.input_frame)
        self.input_box.pack(side='left', fill='x', expand=True, padx=(0, 5))
        self.input_box.bind("<Return>", self.process_user_input)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.process_user_input)
        self.send_button.pack(side='left', padx=(0, 5))

        self.exit_button = tk.Button(self.input_frame, text="Exit", command=self.exit_app, fg="red")
        self.exit_button.pack(side='right')

        # Initial message (FIXED)
        self.write_to_chat("\nPyBot: Hello, I'm PyBot! How can I help you?\n\n", 'bot')

    def write_to_chat(self, text, tag):
        """Helper function to insert text and manage widget state."""
        self.chat_window.config(state='normal')
        self.chat_window.insert(tk.END, text, tag)
        self.chat_window.config(state='disabled')
        self.chat_window.yview(tk.END)

    def process_user_input(self, event=None):
        """Handles user input and generates a bot response."""
        user_input = self.input_box.get()
        if not user_input.strip():
            return

        # Display the user's message with a newline and then an empty line.
        self.write_to_chat(f"You: {user_input}\n\n", 'user')
        self.input_box.delete(0, tk.END)
        self.master.after(500, lambda: self.generate_bot_response(user_input))

    def exit_app(self):
        """Asks for confirmation before closing the application."""
        if messagebox.askyesno("Exit", "Do you want to close the PyBot app?"):
            self.master.destroy()

    def generate_bot_response(self, user_input):
        """Generates a response from the chatbot logic."""
        user_input_lower = user_input.lower()
        response = None

        # Check for weather queries using regex
        weather_match = re.search(r'(weather|temp|temperature)\s+in\s+([\w\s]+)', user_input_lower)
        if weather_match:
            city = weather_match.group(2).strip()
            response = get_real_weather(city)
        
        # Check for live time queries using regex
        time_match = re.search(r'(time|what time is it)\s+in\s+([\w\s]+)', user_input_lower)
        if time_match:
            city = time_match.group(2).strip()
            response = get_live_time(city)

        # Check for memory retrieval
        elif "what is my name" in user_input_lower:
            if "name" in self.user_memory:
                response = f"Your name is {self.user_memory['name'].capitalize()}"
            else:
                response = "I don't know your name yet. You can tell me now."

        # Check for name setting
        elif "my name is" in user_input_lower:
            match = re.search(r'my name is (.+)', user_input_lower)
            if match:
                name = match.group(1).strip()
                self.user_memory['name'] = name
                response = f"Hello, {name.capitalize()}! I'll remember that."

        # Check for math calculation
        elif any(op in user_input_lower for op in ['+', '-', '*', '/', '^']):
            result, error = calculate(user_input_lower)
            response = result if result else error

        # Check for jokes and random facts
        elif "joke" in user_input_lower:
            response = random.choice(jokes)
        elif "fact" in user_input_lower:
            response = random.choice(random_facts)

        # Check general topics using a keyword-based approach
        if not response:
            all_topics = {
                **greetings, **about_chatbot, **motivation_and_study,
                **food, **goodbye_greetings
            }
            for key, values in all_topics.items():
                if any(keyword in user_input_lower for keyword in key.split()):
                    if isinstance(values, list):
                        response = random.choice(values)
                    else:
                        response = values
                    break

        # Fallback response if no match is found
        if not response:
            response = random.choice(fallback_responses)

        self.animate_response(f"PyBot: {response}\n\n")

    def animate_response(self, text, index=0):
        """
        Creates a typing animation for the bot's response.
        Displays one character at a time with a delay.
        """
        if index < len(text):
            self.write_to_chat(text[index], 'bot')
            self.master.after(25, self.animate_response, text, index + 1)
        else:
            # When the animation is complete, add a final newline to ensure the next message starts on a new line
            self.chat_window.insert(tk.END, "")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()



