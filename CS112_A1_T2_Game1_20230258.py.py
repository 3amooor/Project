# File: CS112_A1_T2_2_20230258.py
# Purpose: The game is a competition between two players so each add a number from 1 to 10 then the other do the same thing and add them both untill one of them reach 100
# Author: Omar Tarek Moustafa
# ID : 20230258
def valid_move(current_sum, move):
#checks if the move is valid
    return 1 <= move <= 10 and current_sum + move <= 100

def update_game_status(current_sum, move):
#here it adds the move to the current sum
    return current_sum + move

def display_game_status(current_sum, player):
#here it decide which player to move and what is the current sum
    print(f"Current sum: {current_sum}")
    print(f"It's Player {player}'s turn.")

def check_win(current_sum):
#checks if someone won
    return current_sum == 100


def get_player_move(current_sum, player):
#here it makes every player play a valid integer number
    valid_moves = [m for m in range(1, 11) if valid_move(current_sum, m)]

    while True:
        try:
            move = int(input(f"Player {player}, enter your move from {valid_moves}: "))
            if move in valid_moves:
                return move
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
#here we start the game
    current_sum = 0
    player = 1

    while True:
        #At first it shows the valid numbers and which player move
        display_game_status(current_sum, player)
        move = get_player_move(current_sum, player)

        current_sum = update_game_status(current_sum, move)

        if check_win(current_sum):
            print(f"Player {player} wins!")
            break

        player = 2 if player == 1 else 1

if __name__ == "__main__":
    main()




