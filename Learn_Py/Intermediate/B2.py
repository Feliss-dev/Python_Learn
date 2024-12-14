#Bài tập 2: Tạo danh sách số ngẫu nhiên và tìm số lớn nhất, nhỏ nhất.

import random

random_numbers = [random.randint(1, 100) for _ in range(10)]
print(f"Danh sách số ngẫu nhiên: {random_numbers}")
print(f"Số lớn nhất: {max(random_numbers)}")
print(f"Số nhỏ nhất: {min(random_numbers)}")