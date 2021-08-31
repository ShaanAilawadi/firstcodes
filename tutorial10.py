game = [[1, 0, 2],
        [1, 2, 0],
        [2, 2, 1], ]


def win(current_game):
    # Horizontal
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner horizontally!")


# Diagonal
diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])
if diags.count(diags[0]) == len(diags) and diags[0] != 0:
    print(f"Player {diags[0]} is the winner diagonally (/) !")

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally (\\)!")

    # Vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner vertically (|)!")


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("     0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2,", e)

    except Exception as e:
        print("Something went very wrong!", e)


players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    while not game_won:
        column_choice = input("what column do you want to play? (0, 1, 2): ")
        row_choice = input("What column do you want to play? (0, 1, 2): ")
        game = game_board(game, current_player, row_choice, column_choice)






#game = game_board(game, just_display=True)
#game = game_board(game, player=1, row=2, column=1)
