import random

HANGMAN_PICS = [
    """
      +---+
          |
          |
          |
         ===""",
    """
      +---+
      O   |
          |
          |
         ===""",
    """
      +---+
      O   |
      |   |
          |
         ===""",
    """
      +---+
      O   |
     /|   |
          |
         ===""",
    """
      +---+
      O   |
     /|\\  |
          |
         ===""",
    """
      +---+
      O   |
     /|\\  |
     /    |
         ===""",
    """
      +---+
      O   |
     /|\\  |
     / \\  |
         ==="""
]

class HangmanGame:
    def __init__(self):
        self.word_dict = {
            "python": "A popular programming language 🐍",
            "galaxy": "A massive system of stars 🌌",
            "laptop": "A portable computer 💻",
            "elephant": "The largest land animal 🐘",
            "quantum": "A branch of physics dealing with subatomic particles ⚛️",
            "planet": "Orbits a star like the Earth 🌍",
            "rocket": "Used to launch satellites 🚀",
            "science": "Systematic study of nature 🔬",
            "gravity": "Force that pulls objects down 🌏",
            "energy": "Ability to do work ⚡",
            "network": "Connected group of computers 🌐",
            "binary": "Uses 0 and 1 in computing 💾",
            "module": "Reusable piece of code in Python 🧩",
            "system": "A group of connected components 🔄",
            "function": "Reusable block of code 🔁",
            "variable": "Used to store data in code 📦",
            "object": "Instance of a class in OOP 🧱",
            "syntax": "Rules of writing code correctly 📚",
            "integer": "Whole number in math 🔢",
            "float": "Decimal number in programming 🔣",
            "boolean": "Data type with True or False 🟢🔴",
            "compile": "Convert code to executable 🔧",
            "debug": "Fixing errors in code 🐞",
            "output": "Result shown to the user 📤",
            "input": "Data entered by the user 📥",
            "random": "Unpredictable or chosen by chance 🎲",
            "import": "Used to bring in modules 📦",
            "loop": "Repeats a block of code 🔁",
            "while": "Loop that runs with condition ⏳",
            "forloop": "Repeats for a known number of times 🔂",
            "recursion": "Function calling itself 🔄",
            "nested": "Something inside something else 📦📦",
            "condition": "A check using if/else ✅❌",
            "return": "Gives back a result from a function ↩️",
            "string": "Text in programming ✍️",
            "method": "Function inside a class 🏷️",
            "class": "Defines blueprint of an object 🧰",
            "inherit": "Getting features from parent class 🧬",
            "override": "Replacing parent method in subclass 🔁",
            "encapsulate": "Hiding data details inside a class 🔐",
            "stack": "Last in, first out structure 📚",
            "queue": "First in, first out structure 🎟️",
            "graph": "Data structure with nodes and edges 🔗",
            "tree": "Hierarchical data structure 🌲",
            "array": "Fixed-size list of items 📏",
            "matrix": "2D array used in math 🎯",
            "vector": "Quantity with direction and magnitude ➡️",
            "search": "Looking for data 🔍",
            "sort": "Arrange data in order 🔃",
            "merge": "Combine two things into one 🔗",
            "insert": "Add a value 📥",
            "delete": "Remove a value ❌",
            "update": "Change existing data ✏️",
            "index": "Position of element in list 📍",
            "pointer": "Stores address of variable 📌",
            "address": "Memory location in computer 🧠",
            "memory": "Stores data in computer 🗃️",
            "cache": "Stores frequently used data 🔁",
            "virtual": "Not real but simulated 💻",
            "thread": "Smallest unit of a process 🧵",
            "process": "Program in execution ⚙️",
            "kernel": "Core of operating system 🧠",
            "driver": "Software to control hardware 🚗",
            "device": "Any hardware like phone, printer etc 📱",
            "server": "Provides services to clients 🌐",
            "client": "Requests services from a server 🙋",
            "cloud": "Internet-based storage ☁️",
            "remote": "Access from far away 🌍",
            "storage": "Saves digital data 💽",
            "backup": "Copy of data for safety 📦",
            "secure": "Free from danger or attack 🔐",
            "encrypt": "Scramble data for protection 🛡️",
            "decrypt": "Convert back scrambled data 🔓",
            "access": "Permission to use something 🧾",
            "admin": "Has full control over system 🧑‍💻",
            "login": "Sign into an account 🔑",
            "logout": "Sign out of account 🚪",
            "session": "Time during which user is active ⏰",
            "cookie": "Stores user data in browser 🍪",
            "script": "File with program instructions 📜",
            "markup": "Used in HTML for formatting 🏷️",
            "layout": "Arrangement of UI elements 📐",
            "design": "Visual appearance of an app 🎨",
            "widget": "Reusable UI component 🧩",
            "button": "Clickable element in UI 🖲️",
            "slider": "Allows user to adjust values 🎚️",
            "canvas": "Drawing area in graphics 🖼️",
            "sprite": "2D image in a game 🎮",
            "render": "Process of drawing graphics 🖌️",
            "shader": "Program that calculates pixels 💡",
            "camera": "Captures visual input 📷",
            "sensor": "Detects physical input 📡",
            "signal": "Transmitted data 📶",
            "pixel": "Smallest unit in a display 🧱",
            "sample": "Small part of a larger data set 🧪",
            "frame": "Single still image in video 🎞️",
            "motion": "Movement over time 🏃",
            "fusion": "Merging of two or more data sources 🔗",
            "detect": "Identify presence of something 🕵️",
            "recognize": "Identify from memory 👁️",
            "model": "Trained data structure in AI 🧠",
            "dataset": "Collection of related data 📊",
            "train": "Teaching AI using data 🚆",
            "predict": "Guess future outcome 🔮"
        }

        self.max_attempts = len(HANGMAN_PICS) - 1
        self.reset_game()

    def reset_game(self):
        self.secret_word, self.hint = random.choice(list(self.word_dict.items()))
        self.correct_letters = set()
        self.wrong_letters = set()
        self.attempts = 0

    def display_game_state(self):
        print(HANGMAN_PICS[self.attempts])
        word_display = " ".join([letter if letter in self.correct_letters else "_" for letter in self.secret_word])
        print(f"\n🧠 Hint: {self.hint}")
        print(f"Word: {word_display}")
        print(f"Wrong guesses ({self.attempts}/{self.max_attempts}): {', '.join(sorted(self.wrong_letters))}")

    def get_player_guess(self):
        while True:
            guess = input("\nEnter a letter: ").lower().strip()
            if len(guess) != 1 or not guess.isalpha():
                print("⚠️  Please enter a single alphabet letter.")
            elif guess in self.correct_letters or guess in self.wrong_letters:
                print("⚠️  You already guessed that letter.")
            else:
                return guess

    def update_game_state(self, guess):
        if guess in self.secret_word:
            self.correct_letters.add(guess)
            print("✅ Good guess!")
        else:
            self.wrong_letters.add(guess)
            self.attempts += 1
            print("❌ Oops! That letter is not in the word.")

    def is_game_won(self):
        return all(letter in self.correct_letters for letter in self.secret_word)

    def is_game_lost(self):
        return self.attempts >= self.max_attempts

    def play(self):
        self.reset_game()
        print("\n🎮 Welcome to Master-Level Hangman with Hints!")

        while not (self.is_game_won() or self.is_game_lost()):
            self.display_game_state()
            guess = self.get_player_guess()
            self.update_game_state(guess)

        self.display_game_state()
        if self.is_game_won():
            print(f"\n🎉 Congratulations! You guessed the word: {self.secret_word}")
        else:
            print(f"\n💀 Game Over! The correct word was: {self.secret_word}")

def main():
    while True:
        game = HangmanGame()
        game.play()
        replay = input("\n🔁 Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("\n👋 Thanks for playing Hangman. Goodbye!")
            break

if __name__ == "__main__":
    main()
