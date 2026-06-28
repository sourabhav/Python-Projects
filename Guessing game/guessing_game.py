import random

easy_words= [ "india", "book", "school", "city", "cat", "food" ]
medium_words= [ "university", "bangalore", "laptop", "earth"]
hard_words= [ "knowledge", "playground", "diamond", "maountain"]

print("WELCOME TO PASSWORD GUESSING GAME!")
print("Choose the difficulty level- easy/medium/hard :")

level= input("Enter difficulty: ").lower()
if level=="easy":
    secret=random.choice(easy_words)
elif level=="medium":
    secret=random.choice(medium_words)
elif level=="hard":
    secret=random.choice(hard_words)  
else:
    print("Invalid choice- defaulting to EASY LEVEL")
    secret=random.choice(easy_words)

attempts=0
print("--Guess the secret password--")

while True:
    guess= input("Enter your guess: ").lower()
    attempts+=1

    if guess==secret:
        print(f"CONGRATULATIONS! you gessed it coorect in {attempts} attempts")
        break
    
    hint = ""

    for i in range(len(secret)):
        if i<len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("HINT:", hint)      
print("GAME OVER!")      

    