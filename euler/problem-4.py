def digits(num):
    temp = num
    res = 0
    while (temp > 0):
        temp = int(temp / 10)
        res += 1
    return res
    
def arrayize(num):
    lenn = digits(num)
    res = []
    for i in range(lenn):
        temp = int(num % 10)
        res.append(temp)
        num /= 10
    return res
    
def is_palindromic(num):
    arr = arrayize(num)
    arr_rev = arr.copy()
    arr_rev.reverse()
    if (arr == arr_rev):
        return True
    else:
        return False
    
def main():
    import numpy as np
    three_digits_1 = np.arange(100,1000)
    all_possible = []
    for first in three_digits_1:
        for second in three_digits_1:
            if (is_palindromic(first * second)):
                all_possible.append(first * second)
    print(np.amax(all_possible))
    
if (__name__ == '__main__'):
    main()