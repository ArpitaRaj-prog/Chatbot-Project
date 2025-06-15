import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name ?",
        ["I am your friendly chatbot.", "You can call me ArpitaBot."]
    ],
    [
        r"how are you ?",
        ["I'm doing great! Thanks for asking.", "I am fine, how can I help you?"]
    ],
    [
        r"(.*) your creator ?",
        ["I was created by Arpita.", "My creator is Arpita."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I live on Arpita's computer.", "I am in the digital world."]
    ],
    [
        r"what is NLP ?",
        ["NLP stands for Natural Language Processing. It helps computers understand human language."]
    ],
    [
        r"(.*) help (.*)",
        ["I can answer your questions and chat with you!"]
    ],
    [
        r"quit",
        ["Bye! Have a nice day.", "Goodbye!"]
    ]
]

chatbot = Chat(pairs, reflections)

print("Hello! I'm ArpitaBot. Type 'quit' to exit.")
chatbot.converse()