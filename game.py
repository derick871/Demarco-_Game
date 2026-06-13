import os
import random
import sqlite3
import pandas as pd

# ==========================================
# CONFIGURATION
# ==========================================

DB_NAME = "game_data.db"
EXCEL_NAME = "leaderboard.xlsx"

SECRET_NUMBERS = [24, 33, 51, 98, 70, 81]

# ==========================================
# DATABASE FUNCTIONS
# ==========================================

def init_db():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS high_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_to_database(username, score):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO high_scores (username, score)
        VALUES (?, ?)
        """,
        (username, score)
    )

    conn.commit()
    conn.close()


# ==========================================
# EXCEL FUNCTIONS
# ==========================================

def export_to_excel():
    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query(
        """
        SELECT username, score
        FROM high_scores
        ORDER BY score DESC
        """,
        conn
    )

    conn.close()

    df.to_excel(EXCEL_NAME, index=False)

    print(f"\n Data exported to '{EXCEL_NAME}'")


def save_score(username, score):
    save_to_database(username, score)
    export_to_excel()


# ==========================================
# LEADERBOARD
# ==========================================

def show_leaderboard():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT username, score
        FROM high_scores
        ORDER BY score DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()

    conn.close()

    print("\n===== LEADERBOARD =====")

    if not rows:
        print("No scores recorded yet.")
        return

    for position, (username, score) in enumerate(rows, start=1):
        print(f"{position}. {username} - {score} points")


# ==========================================
# GAME FUNCTIONS
# ==========================================

def get_difficulty():

    print("\nChoose Difficulty")
    print("1. Easy (7 tries)")
    print("2. Medium (5 tries)")
    print("3. Hard (4 tries)")

    while True:

        choice = input("Choose level (1-3): ").strip()

        if choice == "1":
            return "Easy", 7

        elif choice == "2":
            return "Medium", 5

        elif choice == "3":
            return "Hard", 4

        print("Invalid choice. Try again.")


def give_hint(number):

    print("\n===== HINT =====")

    if number % 2 == 0:
        print(" The number is EVEN")
    else:
        print(" The number is ODD")

    if number % 9 == 0:
        print(" Divisible by 9")
    elif number % 7 == 0:
        print(" Divisible by 7")
    else:
        print(" Not divisible by 7 or 9")

    print("================")


# ==========================================
# MAIN GAME
# ==========================================

def play_game():

    print("=" * 30)
    print("     DEMARCO GAME")
    print("=" * 30)

    username = input("\nEnter your name: ").strip()

    difficulty_name, attempts_allowed = get_difficulty()

    # Select one of the predefined numbers
    secret_number = random.choice(SECRET_NUMBERS)

    attempts_used = 0
    wrong_guesses = 0
    won = False

    while attempts_used < attempts_allowed:

        try:
            guess = int(input("\nEnter your guess (1-100): "))

            if guess < 1 or guess > 100:
                print(" Number must be between 1 and 100.")
                continue

        except ValueError:
            print(" Please enter a valid integer.")
            continue

        attempts_used += 1
        remaining = attempts_allowed - attempts_used

        if guess == secret_number:

            score = (attempts_allowed - attempts_used + 1) * 10

            print(f"\n Congratulations {username}!")
            print(f"Difficulty: {difficulty_name}")
            print(f"Attempts Used: {attempts_used}")
            print(f"Score: {score}")

            save_score(username, score)

            won = True
            break

        elif guess > secret_number:
            print(" Too High!")

        else:
            print(" Too Low!")

        wrong_guesses += 1

        if wrong_guesses == 3:
            give_hint(secret_number)

        print(f"Remaining guesses: {remaining}")

    if not won:

        print("\n Game Over!")
        print(f"The correct number was {secret_number}")

        save_score(username, 0)

    show_leaderboard()




if __name__ == "__main__":

    init_db()

    try:
        play_game()

    except KeyboardInterrupt:
        print("\n\nGame terminated .")