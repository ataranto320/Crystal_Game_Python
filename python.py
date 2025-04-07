import random

# Variables
wins = 0
losses = 0
total = 0
Random = random.randint(19, 120)

# Gem values
gem1 = random.randint(1, 12)
gem2 = random.randint(1, 12)
gem3 = random.randint(1, 12)
gem4 = random.randint(1, 12)

def reset():
    global Random, gem1, gem2, gem3, gem4, total
    Random = random.randint(19, 120)
    print(f"New random number: {Random}")
    gem1 = random.randint(1, 12)
    gem2 = random.randint(1, 12)
    gem3 = random.randint(1, 12)
    gem4 = random.randint(1, 12)
    total = 0
    print(f"Total reset to: {total}")

def check():
    global wins, losses, total
    if total == Random:
        print("You win!")
        wins += 1
        print(f"Wins: {wins}")
        reset()
    elif total > Random:
        print("You lose!")
        losses += 1
        print(f"Losses: {losses}")
        reset()

# Game loop
def game():
    global total
    print(f"Random Number: {Random}")
    print("Gem values are hidden. Click on gems to add to your total.")
    
    while True:
        # Get user input for which gem to click
        print(f"Current total: {total}")
        print("Choose a gem to add to your total:")
        print("1. Gem 1")
        print("2. Gem 2")
        print("3. Gem 3")
        print("4. Gem 4")
        
        choice = input("Enter 1, 2, 3, or 4 (or 'exit' to quit): ")
        
        if choice == '1':
            total += gem1
        elif choice == '2':
            total += gem2
        elif choice == '3':
            total += gem3
        elif choice == '4':
            total += gem4
        elif choice.lower() == 'exit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please choose 1, 2, 3, or 4.")
            continue
        
        check()

# Start the game
game()
