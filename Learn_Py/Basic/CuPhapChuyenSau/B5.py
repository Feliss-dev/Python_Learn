#Ví dụ: Tính tổng các số lẻ trong danh sách sử dụng list comprehension.
#Ví Ví dụ: Tính tổng các số lẻ trong danh sách sử dụng tính năng hiểu danh sách
numbers = [10, 15, 20, 25, 30, 35, 40]
#tim so le
odd_sum = sum([num for num in numbers if num % 2 != 0]) 
print(f"Tổng các số lẻ trong danh sách là: {odd_sum}")
print(type(odd_sum)) # in ra kiểu dữ liệu

