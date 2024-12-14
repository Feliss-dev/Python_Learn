# Bài 1: Chương trình sử dụng input() để nhận dữ liệu từ người dùng,
#  sau đó chuyển đổi chuỗi nhập vào thành danh sách các số nguyên bằng cách 
# sử dụng split() và int(). sum() tính tổng các số, và trung bình được tính bằng cách
#  chia tổng cho số lượng phần tử trong danh sách (len(numbers)).

numbers = input("Enter a list of numbers with a space between: ").split()



numbers = [int(num) for num in numbers]

print(f"List of numbers: {numbers} ")

total = sum(numbers)

average = total / len(numbers)

print(f"Total: {total}")
print(f"Trung binh : {average}")