'''
    For this video on codon:  https://www.youtube.com/watch?v=chkHgLH_KVU
    اسکریپت‌های پایتونی‌تون رو با کامپایل کردن، تا صد برابر سریعتر کنین

    Final result: It's true, for this great count it enhanced the program 240 times. In fact reduced 6s to 24ms!
    The exe file is attached. It was created using codon.
'''
def is_prime(n):
    for i in range(2, int(n/2)+1):
        if (n % i ==0):
            return False
        return True

count = 0
for i in range(2, 10000000):
    if (is_prime(i)):
        count += 1
print(count)
