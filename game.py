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
        



leaderboard()