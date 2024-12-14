# 2. Viết Generator tạo dãy Fibonacci
# Yêu cầu: Viết hàm generator trả về n số trong dãy Fibonacci.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

for num in fibonacci(10):
    print(num, end=" ")