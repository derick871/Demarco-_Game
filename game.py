import random
import os
def save_score(username, score):
    with open("highScore.txt","a") as file:
      file.write(f"{username},{score}\n")
print(save_score)