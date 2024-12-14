#3. Cấu trúc điều khiển nâng cao
# Ví dụ: Tìm số lớn nhất trong danh sách bằng cách sử dụng cấu trúc điều khiển
numbers = [3, 45, 2, 89, 1, 22, 34]

max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

print(f"Số lớn nhất trong danh sách là: {max_num}")