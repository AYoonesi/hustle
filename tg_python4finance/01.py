"""
    چالش شماره 1- برنامه ای بنویسید که یک ورودی از کاربر دریافت کند و تشخیص دهید که آیا این ورودی عدد صحیح است یا عدد اعشاری یا رشته.
    برنامه خود را در کامنت های ذیل این پست ضمیمه کنید. دقت کنید که برنامه شما با برنامه های قبلی ارسال شده متفاوت باشد.
    #پایتون_عمومی
    #سطح_آسان
"""

def main():
    inp = input('some shit:')
    try:
        print('try:  int' if(int(float(inp) * 10) == int(float(inp)) * 10) else 'float')
    except:
        print('except:  str')
if(__name__ == '__main__'):
    main()