import os
from race_engine.models import Horse, ProHorse
from race_engine.validators import validate_bet

def start_race():
    
    print("\n==============================")
    print("    HORSE SELECTION MENU")
    print("==============================")
    print("1: Standard Horse (Normal speed)")
    print("2: Pro Horse (Bonus speed!)")
    
    choice = input("\nSelect 1 or 2: ")

    
    if choice == "2":
        my_horse = ProHorse("Lightning")
        print(f"\n>>> You have selected the PRO HORSE: {my_horse.name}")
    else:
       
        my_horse = Horse("Slowpoke")
        print(f"\n>>> You have selected the STANDARD HORSE: {my_horse.name}")

  
    print("-" * 30)
    bet_input = input("Enter your bet amount (e.g., 100 or £100): ")
    
    
    validated_amount = validate_bet(bet_input)

    if validated_amount is not None:
       
        score = my_horse.get_speed()
        
        print(f"\nRace finished!")
        print(f"Final Score: {score}")
        print("-" * 30)
        if not os.path.exists('data'): 
            os.makedirs('data')
            
        with open("data/results.txt", "a") as f:
           
            f.write(f"Horse: {my_horse.name}, Bet: {validated_amount}, Score: {score}\n")
            
        print("Data logged successfully to data/results.txt")
    else:
        print("\nError: Invalid bet. Please use numbers (the £ sign is allowed).")

if __name__ == "__main__":
    start_race()