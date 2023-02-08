# Rock Scissors Paper

import random

def game_over():
    print('Game over')

def game_start():
    print('welcome to the game of rocks')
    return int(input('How many times do you wanna play?\n'))
   
def score_calculations(what_to_do = 'none'):
    if (what_to_do == 'Human'):
        print('You: +1')
        return {'Human': 1, 'Computer': 0}
    elif (what_to_do == 'Computer'):
        print('Computer: +1')
        return {'Human': 0, 'Computer': 1}
    elif (what_to_do == 'none'):
        print('Mosavi')
        return {'Human': 0, 'Computer': 0}
    
def mission_one():
    print('ROCK, PAPER OR SCISSORS? 0/1/2')
    human_choice = int(input())
    computer_choice = random.randint(0, 2)
    if (human_choice == computer_choice):
        res = score_calculations('none')
        return ['----', res]
    match human_choice:
        case 0:
            if (computer_choice == 2):
                res = score_calculations('Human')
            else:
                res = score_calculations('Computer')
        case 1:
            if (computer_choice == 0):
                res = score_calculations('Human')
            else:
                res = score_calculations('Computer')
        case 2:
            if (computer_choice == 1):
                res = score_calculations('Human')
            else:
                res = score_calculations('Computer')
    return ['----', res]

def rolling_game(times):
    scores = {'Human': 0, 'Computer': 0}
    for index in range(times):
        print(f'* Round {index + 1} *')
        tmp = mission_one()
        print(tmp[0])
        scores['Computer'] += tmp[1]['Computer']
        scores['Human'] += tmp[1]['Human']
    return scores
    
def who_is_the_winner(you, him):
    if (you > him):
        return 'you won'
    elif (you < him):
        return 'the computer won'
    else:
        return 'the game is mosavi'
    
def main():
    how_many_times = game_start()
    print('\n---')
    scores = rolling_game(how_many_times)
    you = scores['Human']
    him = scores['Computer']
    who_won = ['you won', 'computer won', 'Mosavi']
    who_won = who_is_the_winner(you, him)
    print(f'\nYou got {you} and the computer got. {him}\nWhich means that {who_won}.')
    return 0

main()