'''
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a**2 + b**2 = c**2
    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

    --

    I know taht the root of 1000 is about 31.62, so it must be between 
'''

def main():
    import math
    import numpy as np
    is_found = False
    for n in range(int(1000 / 2)):
        for m in range(int(1000 / 2)):
            tmp = 1000 - n - m
            if (n **2 + m ** 2 == tmp ** 2):
                print(n,m, tmp)
                is_found = True
                print(n*m*tmp)
        if (is_found):
            break

if (__name__ == '__main__'):
    main()