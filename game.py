import os
import random

def save_score(username, score):
    with open("highScores.txt", "a") as file:
        file.write(f"{username},{score}\n")

def leaderboard():
    print("\n===== LEADERBOARD =====")

    if not os.path.exists("highScores.txt"):
        print("No scores recorded!")

    scores = []

    with open("highScores.txt", "r") as file:
        for line in file:
            name, score = line.strip().split(",")
            scores.append((name, int(score)))

    scores.sort(key=lambda x: x[1], reverse=True)

    for position, (name, score) in enumerate(scores[:10], start=1):
        print(f"{position}. {name} - {score} points")

def get_diffuculty():
    print("\nChoose levels")
    print("1.Easy(7 trials)")
    print("2.Medium(5 trials)")
    print("3.Hard(4 trials)")

    while True:
        choice=input("choose your level")
        if choice =="1":
          return 7
        elif choice =="2":
            return 5
        elif choice =="3":
            return 4
        else:
            print("Invalid choice,Try again")
print("level selections")

def give_hint(number):
    print("\n===hint===")
    if number % 2:
        print("Is even number")
    else:
        print("Is an odd number")
    if number % 9:
        print("Divisible by 9")
    elif number % 7:
        print("Divisible by 7")
    else:
        print("Not divisible by both 9 and 7")
        
print("==================")
print("===Demarco Game===")
print("==================")

username=input("Enter your name")
attempts_allowed=get_diffuculty()
secret_numbers= random.randint(1,100)

attempts_used= 0
wrong_guesses= 0
win= False

while attempts_used < attempts_allowed:
    try:
        guess= int(input("\n Enter your numbers(1-100):"))
        if guess >100:
            print("Out of range")
    except ValueError:
        print("enter a valid value")
        continue


leaderboard()