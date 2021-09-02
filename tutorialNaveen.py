import itertools

'''
game = [[1, 0, 2],
        [2, 2, 2],
        [1, 2, 1], ]
'''


def win(current_game):
    # Horizontal
    for row in current_game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    # Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally (/) !")
        return True

        diags = []
        for ix in range(len(current_game)):
            diags.append(current_game[ix][ix])
        if diags.count(diags[0]) == len(diags) and diags[0] != 0:
            print(f"Player {diags[0]} is the winner diagonally (\\)!")
            return True

    # Vertical
    for col in range(len(current_game)):
        check = []

        for row in current_game:
            check.append(row[col])

        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner vertically (|)!")
            return True

    # bottom of function, not yet returned
    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2,", e)

    except Exception as e:
        print("Something went very wrong!", e)


if __name__ == "__main__":
    play = True
    players = [1, 2]
    while play:
        game = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        game_won = False
        game = game_board(game, just_display=True)
        player_choice = itertools.cycle([1, 2])
        while not game_won:
            current_player = next(player_choice)
            print(f"Current Player: {current_player}")
            column_choice = int(
                input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(
                input("What row do you want to play? (0, 1, 2): "))
            game = game_board(game, current_player, row_choice, column_choice)

            # check if your won
            game_won = win(game)


#game = game_board(game, just_display=True)
#game = game_board(game, player=1, row=2, column=1)
