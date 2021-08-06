import random

def main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    rounds = 1

    while rounds != 6:
        print(f"-Round- {rounds}")
        player1 = diceRoll()
        player2 = diceRoll()
        print(f"Player 1 is rolling {player1}")
        print(f"Player 2 is rolling {player2}")

        if player1 == player2:
            print("It's a draw!\n")
        elif player1 > player2:
            player1wins = player1wins + 1
            print("Player 1 wins!\n")
        else:
            player2wins = player2wins + 1
            print("Player 2 wins\n")

        rounds = rounds + 1

    if player1wins == player2wins:
        print("Tie!\n")
    elif player1wins > player2wins:
        print(f"Player 1 wins with the score of {player1wins}!\n")
    else:
        print(f"Player 2 wins with the score of {player2wins}!\n")        

def diceRoll():
    diceRoll = random.randint(1,6)
    return diceRoll

main()