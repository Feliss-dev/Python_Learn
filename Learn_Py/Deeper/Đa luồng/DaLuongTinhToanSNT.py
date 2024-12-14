# #Bài 2: Tính toán số nguyên tố sử dụng đa luồng
# Mô tả
# Chia một khoảng số thành nhiều phần.
# Sử dụng các luồng để kiểm tra số nguyên tố trong mỗi phần.


import threading

#Ham kiem tra so nguyen to
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Ham xu ly tim so nguyen to trong khoang
def find_primes(start, end):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    print(f"Found {len(primes)} primes between {start} and {end}\n")
    print(f"Chuoi so nguyen to: {primes}")

# Chia khoang so thanh 5 phan
ranges = [(2, 100), (100, 200), (200, 300), (300, 400), (400, 500)]
print(type(ranges))

# tao luong
threads = []

for start, end in ranges:
    thread = threading.Thread(target=find_primes, args=(start, end))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

