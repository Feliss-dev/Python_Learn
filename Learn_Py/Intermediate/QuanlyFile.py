#Viết chương trình tạo 100 file văn bản, mỗi file chứa một số ngẫu nhiên 
# từ 1 đến 1000. Sau đó, đọc lại các file và tính tổng các số.

import os
import random

os.makedirs("random_files", exist_ok=True)

# Tạo file
for i in range(1, 101):
    with open(f"random_files/file_{i}.txt", "w") as file:
        file.write(str(random.randint(1, 1000)))

# Đọc và tính tổng
total = 0
for i in range(1, 101):
    with open(f"random_files/file_{i}.txt", "r") as file:
        total += int(file.read())

print("Tổng các số:", total)
