import random
import time

def main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    rounds = 1

    while rounds != 6:
        time.sleep(2)
        print(f"Round {rounds}")
        player1 = diceRoll()
        player2 = diceRoll()
        print(f"Player A rolling {player1}")
        time.sleep(3)
        print(f"Player B rolling {player2}")

        if player1 == player2:
            print("Tie!\n")
        elif player1 > player2:
            player1wins = player1wins + 1
            print("Player A wins!\n")
        else:
            player2wins = player2wins + 1
            print("Player B wins!\n")

        rounds = rounds + 1

    if player1wins == player2wins:
        print("Tie!\n")
    elif player1wins > player2wins:
        print(f"Player A wins with {player1wins}\n")
    else:
        print(f"Player B wins with {player2wins}\n")        

def diceRoll():
    diceRoll = random.randint(1,6)
    return diceRoll

main()