import os
from race_engine.models import ProHorse
from race_engine.validators import validate_bet

def start_race():
    my_horse = ProHorse("Lightning")
    print(f"\n--- Horse Racing Simulator ---\nYour horse: {my_horse.name}")
    bet = input("Enter your bet amount (numbers only): ")
    if validate_bet(bet):
        score = my_horse.get_speed()
        print(f"Race finished! Your score: {score}")
        if not os.path.exists('data'): os.makedirs('data')
        with open("data/results.txt", "a") as f:
            f.write(f"Bet: {bet}, Score: {score}\n")
        print("Data logged successfully.")
    else:
        print("Error: Invalid bet. Numbers only.")

if __name__ == "__main__":
    start_race()