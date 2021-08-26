game = [[2, 0, 1],
        [1, 0, 2],
        [2, 2, 1], ]


for col in range(len(game)):
    check = []

for row in game:
    #print (row[0])
    check.append(row[col])

if check.count(check[0]) == len(check) and check[0] != 0:
    print("Winner!")

'''
def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Winner!")


win(game)
'''
