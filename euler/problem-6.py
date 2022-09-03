def bala(my_arr):
    tmp = 0
    for adad in my_arr:
        tmp += (adad ** 2)
    return tmp

def payin(my_arr):
    tmp = 0
    for adad in my_arr:
        tmp += adad
    return (tmp ** 2)

def main():
    import numpy as np
    natural_numbers = np.arange(1, 101)
    print(bala(natural_numbers) - payin(natural_numbers))
    

if (__name__ == '__main__'):
    main()