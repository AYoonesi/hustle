import random

english_letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', '\\', ':', ';', '"', "'", '<', ',', '>', '.', '?', '/']

def greets():
    print('Hell -O- World! ')
    print('--« Welcome to Ran-Dom Pass Gen »--')

def asks():
    print('How many letters? (Minimum: 1, Default: 0)')
    tmp = int(input())
    letters_count = 4 if (tmp < 1) else tmp
    print('How many symbols? (Minimum: 1, Default: 0)')
    tmp = int(input())
    symbols_count = 4 if (tmp < 1) else tmp
    print('And how many nmbers? (Minimum: 1, Default: 0)')
    tmp = int(input())
    numbers_count = 4 if (tmp < 1) else tmp
    return [letters_count, symbols_count, numbers_count]
    
def generate_given(dade):
    password_generated = ''
    for _ in range(dade[0]):
        tmp = random.randint(0, len(english_letters) - 1)
        password_generated += english_letters[tmp]
    for _ in range(dade[1]):
        tmp = random.randint(0, len(numbers) - 1)
        password_generated += numbers[tmp]
    for _ in range(dade[2]):
        tmp = random.randint(0, len(symbols) - 1)
        password_generated += symbols[tmp]
    return password_generated

def pasword_security(given_password: str = 'girTLig5100890_:(,?[%'):
    tmp = [i for i in given_password]
    for _ in range(1000):
        rnd1, rnd2 = random.randint(0, len(tmp) -1), random.randint(0, len(tmp) -1)
        tmp[rnd1], tmp[rnd2] = tmp[rnd2], tmp[rnd1]
    return ''.join(tmp)

def main():
    greets()
    chand_o_choon = asks()
    insecure_password = generate_given(dade=chand_o_choon)
    secured_password = pasword_security(insecure_password)
    print(f'Secure password is: {secured_password}')
    
main()