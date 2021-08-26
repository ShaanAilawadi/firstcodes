import random


def run_game():
    min_number = int(input("minimum number: "))
    max_number = int(input("Max number: "))
    guesses = int(input("Number of guesses: "))
    some_nums = list(range(1, max_number + 1))
    random.shuffle(some_nums)
    selection = some_nums[0]
    user_input = max_number + 5

    guess_count = 0

    try:
        user_input = int(input('guess a number:'))
    except ValueError:
        try:
            user_input = int(input('Try again: '))
        except ValueError:
            print('You are stupid. Learn what a number is retard')
            return
    while user_input != selection:
        guess_count += 1
        if user_input > selection:
            print('Too High')
        elif user_input < selection:
            print('Too Low')
        if guesses == guess_count:
            print('You are a trash can')
            break
        user_input = int(input('try again: '))
        if user_input == selection:
            print('you got it! The number is {selection}.')


run_game()
