"""
    چالش شماره 2- برنامه ای بنویسید که 10 عدد از کاربر دریافت کند و آنها را به ترتیب از کم به زیاد مرتب کرده و میانگین آنها را محاسبه کند.
    سعی کنید از توابع پایتون استفاده نکنید و به صورت دستی کار را انجام دهید.
    برنامه خود را در کامنت های ذیل این پست ضمیمه کنید. دقت کنید که برنامه شما با برنامه های قبلی ارسال شده متفاوت باشد.
    #پایتون_عمومی
    #سطح_آسان
"""
    
from random import randint

def my_input():
    inp = []
    for i in range(2):
        inp.append(int(input()))
    return inp

def my_mean(my_inp):
    sum = 0
    for i in range(len(my_inp)):
        sum += my_inp[i]
    return sum/len(my_inp)

def my_sort(my_inp):
    res = []
    for i in range(len(my_inp)):
        res.append(min(my_inp))
        my_inp.remove(min(my_inp))
    return res

def main():
    # inp = my_input()
    # inp = [1, 2, 3, 4, 5, 6]
    inp = [(randint(1, 1000)) for i in range(10)]
    print('mean:', my_mean(inp))
    print('sorted res:', my_sort(inp))
    
if(__name__ == '__main__'):
    main()