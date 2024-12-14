# #Bài tập tổng hợp
# Viết chương trình quản lý nhật ký hàng ngày:

# Ghi nhật ký vào file (ngày, nội dung).
# Đọc lại nhật ký.
# Đếm tổng số dòng nhật ký đã ghi.

from datetime import datetime

def write_diary():
    with open('Learn_Py\Intermediate\example.txt', 'a') as file:
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        content = input('Nhập nội dung nhật ký: ')
        file.write(f"{date} - {content}\n")
        print('Đã ghi nhật ký')

def read_diary():
    with open('Learn_Py\Intermediate\example.txt', 'r') as file:
        print("Noi dung nhat ky:")
        content = file.read()
        print(content)

def count_entries():
    with open("Learn_Py\Intermediate\example.txt", "r") as file:
        lines = file.readlines()
        print(f"Tổng số dòng nhật ký: {len(lines)}")

#Menu chinh
while True:
        print("\n1. Ghi nhật ký\n2. Đọc nhật ký\n3. Đếm số dòng\n4. Thoát")
        choice = input("Chon chuc nang")
        if choice == "1":
            write_diary()
        elif choice == "2":
            read_diary()
        elif choice == "3":
            count_entries()
        elif choice == "4":
            break
        else:
            print("Chuc nang khong ton tai")
