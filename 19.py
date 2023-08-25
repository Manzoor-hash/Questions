import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Game!")
    
    while True:
        input("Press Enter to roll the dice...")
        dice_value = roll_dice()
        print(f"You rolled a {dice_value}")
        
        choice = input("Do you want to roll again? (y/n): ")
        if choice.lower() != 'y':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()