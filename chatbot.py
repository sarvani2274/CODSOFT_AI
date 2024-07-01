import random

class Chatbot:
    def __init__(self):
        self.user_name = ""
        self.responses = {
            'greeting': ["Hello, {}! How can I assist you today?", "Hi, {}! What can I do for you?", "Hey, {}! Need any help?"],
            'how are you': ["I'm just a program, but I'm doing great!", "I'm functioning as expected! How about you?"],
            'name': ["My name is Chatbot. What's yours?", "I'm Chatbot. And you are?"],
            'bye': ["Goodbye, {}! Have a great day!", "See you later, {}!", "Bye, {}! Take care!"]
        }
        self.sentiment_words = {
            'positive': ['good', 'great', 'awesome', 'fantastic', 'happy'],
            'negative': ['bad', 'sad', 'terrible', 'horrible', 'unhappy']
        }
        self.unknown_responses = ["I'm sorry, I didn't understand that. Can you please rephrase?", "Could you clarify that?", "I'm not sure I follow."]

    def get_response(self, user_input):
        user_input = user_input.lower()
        if not self.user_name:
            for keyword in self.responses['name']:
                if keyword in user_input:
                    return random.choice(self.responses['name'])
            if 'my name is' in user_input:
                self.user_name = user_input.split('my name is ')[1].strip()
                return f"Nice to meet you, {self.user_name}!"
            else:
                return random.choice(self.responses['name'])

        if any(greeting in user_input for greeting in ['hello', 'hi', 'hey']):
            return random.choice(self.responses['greeting']).format(self.user_name)
        elif 'how are you' in user_input:
            return random.choice(self.responses['how are you'])
        elif 'your name' in user_input:
            return f"My name is Chatbot, and I'm here to help you, {self.user_name}."
        elif any(farewell in user_input for farewell in ['bye', 'exit', 'goodbye']):
            return random.choice(self.responses['bye']).format(self.user_name)

        for sentiment in self.sentiment_words['positive']:
            if sentiment in user_input:
                return "I'm glad to hear that!"
        for sentiment in self.sentiment_words['negative']:
            if sentiment in user_input:
                return "I'm sorry to hear that. Is there anything I can do to help?"

        return random.choice(self.unknown_responses)

def main():
    bot = Chatbot()
    print("Hello! I'm a simple chatbot. How can I help you today?")

    while True:
        user_input = input("You: ")
        response = bot.get_response(user_input)
        print(f"Chatbot: {response}")
        if 'bye' in user_input or 'exit' in user_input or 'goodbye' in user_input:
            break

if __name__ == "__main__":
    main()
