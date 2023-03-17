'''
    For this video on codon:  https://www.youtube.com/watch?v=chkHgLH_KVU
    اسکریپت‌های پایتونی‌تون رو با کامپایل کردن، تا صد برابر سریعتر کنین
'''
def is_prime(n):
    for i in range(2, int(n/2)+1):
        if (n % i ==0):
            return False
        return True

count = 0
for i in range(2, 100000):
    if (is_prime(i)):
        count += 1
print(count)
