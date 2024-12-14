# Bài 2: Chương trình kiểm tra một số nguyên có phải là số
#  nguyên tố hay không. Một số nguyên tố là số lớn hơn 1 và
#  không chia hết cho bất kỳ số nào ngoài 1 và chính nó. Chúng ta kiểm tra 
# điều này bằng cách chia số đó cho tất cả các số nhỏ hơn nó (từ 2 đến n-1).

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = int(input("Nhập một số: "))
if isPrime(number):
    print(f"{number} là số nguyên tố")
else:
    print(f"{number} không phải là số nguyên tố")