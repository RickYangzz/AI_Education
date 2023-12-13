import sys
import random
from enum import Enum

def rps(name="Player"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(f'\n{name}, please enter...\n1 for Rock ✊,\n2 for Paper 👋, or\n3 for Scissors:\n\n')
        
        if playerchoice not in  ["1", "2", "3"]:
            print(f"\n{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n{name}, you chose {str(RPS(player)).replace("RPS.", "").title()}.")
        print(f"Python choses {str(RPS(computer)).replace("RPS.", "").title()}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉{name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉{name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉{name}, you win!"
            elif player == computer:
                return "😯 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins! Sorry, {name}...😢"
        
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f"\nGame count: {game_count}\n")
        print(f"{name}\'s wins: {player_wins}")
        print(f"Python\'s wins: {python_wins}")

        print(f"\nPlay again? {name}")

        while True:
            playagain = input("\nY for yes \nQ for quit\n\n")
            if playagain not in ["y", 'q']:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye! {name}👋")

    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the player."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()