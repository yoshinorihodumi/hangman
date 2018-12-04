import random

def hangman():
    word_list = ["Python","Java","computer","hacker","painter"]
    random_number = random.randint(0,4)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["", "_____     ", "|    |     ", "|    0     ", "|   /|\   ", "|   /\    ", "|"]
    remaining_leters = list(word)
    letter_board = ["_"] * len(word)
    win = False
    print('Welcom to Hangman')
    print(len(stages))
    while wrong_guesses < len(stages) -1  :
        guess = input("Guess a letter")
        if guess in remaining_leters:
            character_index = remaining_leters.index(guess)
            letter_board[character_index] = guess
            remaining_leters[character_index] = '$'
        else:
            wrong_guesses += 1
        print(wrong_guesses)
        print((''.join(letter_board)))
        print('\n'.join(stages[0:wrong_guesses + 1]))
        if '_' not in letter_board:
            print('You win! The word was:')
            print(''.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages))
        print('You lose! The words was {}'.format(word))



hangman()
