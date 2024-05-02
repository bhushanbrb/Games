import random

class Beyblade:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return random.randint(1, self.power)

def battle(player1, player2):
    print(f"{player1.name} vs {player2.name}!")
    while True:
        p1_attack = player1.attack()
        p2_attack = player2.attack()

        print(f"{player1.name} attacks with power {p1_attack}")
        print(f"{player2.name} attacks with power {p2_attack}")

        if p1_attack > p2_attack:
            print(f"{player1.name} wins!")
            return player1
        elif p2_attack > p1_attack:
            print(f"{player2.name} wins!")
            return player2
        else:
            print("It's a tie! Let's attack again.")

if __name__ == "__main__":
    beyblades = [
        Beyblade("Dragoon", 100),
        Beyblade("Pegasus", 110),
        Beyblade("Draciel", 120),
        Beyblade("Wyvern", 90)
    ]

    print("Welcome to the Beyblade Battle!")
    print("Choose your Beyblade:")
    for i, beyblade in enumerate(beyblades, 1):
        print(f"{i}. {beyblade.name}")

    while True:
        try:
            choice = int(input("Enter the number of your Beyblade: "))
            if 1 <= choice <= len(beyblades):
                break
            else:
                print("Invalid choice. Please enter a number between 1 and", len(beyblades))
        except ValueError:
            print("Invalid input. Please enter a number.")

    player_beyblade = beyblades[choice - 1]

    opponent_beyblade = random.choice(beyblades)
    while opponent_beyblade == player_beyblade:
        opponent_beyblade = random.choice(beyblades)

    print(f"You've chosen {player_beyblade.name}!")
    winner = battle(player_beyblade, opponent_beyblade)
    print(f"The winner is {winner.name}!")