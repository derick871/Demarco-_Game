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

# Example
save_score("Derrick", 90)
save_score("Brian", 80)

leaderboard()