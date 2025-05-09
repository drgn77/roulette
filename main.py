import random
from art import logo


# Global game state
balance = 100

# European roulette wheel with number-color mapping
roulette_wheel = {
    0: "green",
    1: "red", 2: "black", 3: "red", 4: "black", 5: "red", 6: "black",
    7: "red", 8: "black", 9: "red", 10: "black", 11: "black", 12: "red",
    13: "black", 14: "red", 15: "black", 16: "red", 17: "black", 18: "red",
    19: "red", 20: "black", 21: "red", 22: "black", 23: "red", 24: "black",
    25: "red", 26: "black", 27: "red", 28: "black", 29: "black", 30: "red",
    31: "black", 32: "red", 33: "black", 34: "red", 35: "black", 36: "red"
}


def start_game():
    """Main game loop."""
    global balance
    game_running = True
    print(logo)
    print("🎰 Welcome to the Roulette Wheel! 🎰")

    while game_running:
        if balance <= 0:
            print("You have no more money. Game over!")
            break

        print(f"\n💵 Current balance: ${balance}")
        print(
            "\nWhat type of bet would you like to place?\n"
            "1. Bet on a specific number (0–36)\n"
            "2. Bet on color (red/black/green)\n"
            "3. Bet on even or odd\n"
            "4. Bet on range (1–18 or 19–36)"
        )

        choice = input("Enter the number of your choice (1-4): ")
        game_type(choice)

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            game_running = False
            print(f"Game ended. Final balance: ${balance}")


def spin_wheel():
    """Spins the roulette wheel and returns a random number and its color."""
    print('Spinning wheel...')
    number = random.randint(0, 36)
    color = roulette_wheel[number]
    return number, color


def game_type(choice):
    """Handles user selection of bet type."""
    if choice == '1':
        bet_on_number()
    elif choice == '2':
        bet_on_color()
    elif choice == '3':
        bet_on_even_odd()
    elif choice == '4':
        bet_on_range()
    else:
        print("Invalid choice.")


def bet_on_number():
    """Bet on a specific number (payout: 35:1)."""
    global balance
    try:
        bet_number = int(input("Enter the number you want to bet on (0–36): "))
        if bet_number < 0 or bet_number > 36:
            print("Invalid number.")
            return

        bet_amount = int(input("Enter your bet amount: $"))
        if bet_amount > balance or bet_amount <= 0:
            print("Invalid bet amount.")
            return

        number, color = spin_wheel()
        print(f"The wheel landed on {number} ({color})")

        if number == bet_number:
            win = bet_amount * 35
            balance += win
            print(f"You won ${win}! 🎉")
        else:
            balance -= bet_amount
            print("You lost.")

    except ValueError:
        print("Invalid input.")
    print(f"Balance: ${balance}")


def bet_on_color():
    """Bet on a color (red/black = 1:1, green = 35:1)."""
    global balance
    try:
        bet_color = input("Enter your bet color (red/black/green): ").lower()
        if bet_color not in ['red', 'black', 'green']:
            print("Invalid color.")
            return

        bet_amount = int(input("Enter your bet amount: $"))
        if bet_amount > balance or bet_amount <= 0:
            print("Invalid bet amount.")
            return

        number, color = spin_wheel()
        print(f"The wheel landed on {number} ({color})")

        if color == bet_color:
            win = bet_amount * 35 if color == 'green' else bet_amount
            balance += win
            print(f"You won ${win}! 🎉")
        else:
            balance -= bet_amount
            print("You lost.")

    except ValueError:
        print("Invalid input.")
    print(f"Balance: ${balance}")


def bet_on_even_odd():
    """Bet on even or odd number (1:1 payout)."""
    global balance
    try:
        bet_eo = input("Enter even or odd: ").lower()
        if bet_eo not in ['even', 'odd']:
            print("Invalid input.")
            return

        bet_amount = int(input("Enter your bet amount: $"))
        if bet_amount > balance or bet_amount <= 0:
            print("Invalid bet amount.")
            return

        number, color = spin_wheel()
        print(f"The wheel landed on {number} ({color})")

        if number == 0:
            balance -= bet_amount
            print("The ball landed on 0 (green). House wins!")
        elif number % 2 == 0 and bet_eo == 'even':
            balance += bet_amount
            print(f"You won ${bet_amount}! 🎉")
        elif number % 2 == 1 and bet_eo == 'odd':
            balance += bet_amount
            print(f"You won ${bet_amount}! 🎉")
        else:
            balance -= bet_amount
            print("You lost.")

    except ValueError:
        print("Invalid input.")
    print(f"Balance: ${balance}")


def bet_on_range():
    """Bet on range: low (1–18) or high (19–36), payout 1:1."""
    global balance
    try:
        bet_range = input("Bet on range: low (1–18) or high (19–36): ").lower()
        if bet_range not in ['low', 'high']:
            print("Invalid input.")
            return

        bet_amount = int(input("Enter your bet amount: $"))
        if bet_amount > balance or bet_amount <= 0:
            print("Invalid bet amount.")
            return

        number, color = spin_wheel()
        print(f"The wheel landed on {number} ({color})")

        if number == 0:
            balance -= bet_amount
            print("The ball landed on 0 (green). House wins!")
        elif number <= 18 and bet_range == 'low':
            balance += bet_amount
            print(f"You won ${bet_amount}! 🎉")
        elif number >= 19 and bet_range == 'high':
            balance += bet_amount
            print(f"You won ${bet_amount}! 🎉")
        else:
            balance -= bet_amount
            print("You lost.")

    except ValueError:
        print("Invalid input.")
    print(f"Balance: ${balance}")


# Run the game
start_game()
