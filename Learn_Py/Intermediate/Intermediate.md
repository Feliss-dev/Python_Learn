**1. List Comprehension**
List comprehension là cách viết ngắn gọn để tạo danh sách mới từ một danh sách hoặc iterable.

# Lý thuyết:
Cú pháp:
[biểu_thức for biến in iterable if điều_kiện]
Ưu điểm: Ngắn gọn, hiệu quả, dễ đọc.

# Tạo danh sách các số chẵn từ 1 đến 20:
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, ..., 20]

# Nhân đôi các số trong danh sách:
numbers = [1, 2, 3, 4]
doubled = [x * 2 for x in numbers]
print(doubled)  # Output: [2, 4, 6, 8]


**2. Xử lý file**
Làm việc với file là kỹ năng quan trọng để lưu trữ và đọc dữ liệu.

# Lý thuyết:
Mở file: open()
Chế độ:
    "r": Đọc.
    "w": Ghi (xóa nội dung cũ).
    "a": Ghi thêm.
    "r+": Đọc và ghi.
    Đóng file: file.close() hoặc dùng context manager (with).

Ghi nội dung vào file:
with open("example.txt", "w") as file:
    file.write("Xin chào, đây là nội dung file.\nHọc Python thật thú vị!")

Đọc nội dung file:
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

**3. Ngoại lệ**
Giúp chương trình xử lý lỗi mà không bị dừng đột ngột.

Lý thuyết:
try:
    # Code có thể gây lỗi
except LoạiLỗi as e:
    # Xử lý lỗi
finally:
    # Luôn chạy, dù có lỗi hay không
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Lỗi xảy ra: {e}")
finally:
    print("Kết thúc chương trình.")



Phần Trung Cấp: Lý Thuyết và Bài Tập Chi Tiết
1. List Comprehension
List comprehension là cách viết ngắn gọn để tạo danh sách mới từ một danh sách hoặc iterable.

Lý thuyết:
Cú pháp:
python
Sao chép mã
[biểu_thức for biến in iterable if điều_kiện]
Ưu điểm: Ngắn gọn, hiệu quả, dễ đọc.
Ví dụ:
Tạo danh sách các số chẵn từ 1 đến 20:
python
Sao chép mã
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, ..., 20]
Nhân đôi các số trong danh sách:
python
Sao chép mã
numbers = [1, 2, 3, 4]
doubled = [x * 2 for x in numbers]
print(doubled)  # Output: [2, 4, 6, 8]
2. Xử lý file
Làm việc với file là kỹ năng quan trọng để lưu trữ và đọc dữ liệu.

Lý thuyết:
Mở file: open()
Chế độ:
"r": Đọc.
"w": Ghi (xóa nội dung cũ).
"a": Ghi thêm.
"r+": Đọc và ghi.
Đóng file: file.close() hoặc dùng context manager (with).
Ví dụ:
Ghi nội dung vào file:
python
Sao chép mã
with open("example.txt", "w") as file:
    file.write("Xin chào, đây là nội dung file.\nHọc Python thật thú vị!")
Đọc nội dung file:
python
Sao chép mã
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
3. Ngoại lệ
Giúp chương trình xử lý lỗi mà không bị dừng đột ngột.

Lý thuyết:
Cú pháp:
python
Sao chép mã
try:
    # Code có thể gây lỗi
except LoạiLỗi as e:
    # Xử lý lỗi
finally:
    # Luôn chạy, dù có lỗi hay không
Ví dụ:
Xử lý lỗi chia cho 0:
python
Sao chép mã
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Lỗi xảy ra: {e}")
finally:
    print("Kết thúc chương trình.")


**4. Modules và Packages**
Tái sử dụng mã nguồn bằng cách tạo module riêng hoặc import module có sẵn.

Lý thuyết:
    Module: File Python chứa các hàm, biến, hoặc lớp.
    Package: Thư mục chứa nhiều module.
Ví dụ:
Tạo file mymodule.py với hàm tính giai thừa:

# mymodule.py
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

Import và sử dụng
import mymodule

print(mymodule.factorial(5))  # Output: 120

5. Thư viện cần biết
### os: Làm việc với file và thư mục
Ví dụ: Liệt kê các file trong thư mục hiện tại:

    import os

    files = os.listdir(".")
    print("Các file trong thư mục hiện tại:", files)

### datetime: Xử lý thời gian
Ví dụ: Lấy ngày giờ hiện tại:

    from datetime import datetime

    now = datetime.now()
    print("Thời gian hiện tại:", now.strftime("%Y-%m-%d %H:%M:%S"))

random: Tạo số ngẫu nhiên
Ví dụ: Sinh số ngẫu nhiên từ 1 đến 100:

    import random

    random_number = random.randint(1, 100)
    print(f"Số ngẫu nhiên: {random_number}")

1. List Comprehension
Lý thuyết nâng cao
Lồng nhau (Nested List Comprehension): Dùng khi cần xử lý danh sách 2 chiều hoặc phức tạp.
Kết hợp với hàm: Có thể sử dụng hàm hoặc lambda trong biểu thức.
Tích hợp điều kiện phức tạp: Sử dụng nhiều điều kiện trong một list comprehension.
Ví dụ nâng cao
Tạo ma trận 3x3:

    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(matrix)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

range(1, 4): Tạo ra dãy số [1, 2, 3].
i * j: Tính tích của i và j tại mỗi vòng lặp.
Kết quả cuối cùng sẽ là một ma trận 3x3 (danh sách lồng danh sách), trong đó:

Dòng thứ nhất là tích của 1 với 1, 2, 3.
Dòng thứ hai là tích của 2 với 1, 2, 3.
Dòng thứ ba là tích của 3 với 1, 2, 3.
Phân tích từng vòng chạy
Vòng lặp bên ngoài: for i in range(1, 4)

i lần lượt nhận các giá trị: 1, 2, 3.
Mỗi lần i thay đổi, vòng lặp bên trong chạy trọn vẹn.
Vòng lặp bên trong: for j in range(1, 4)

j lần lượt nhận các giá trị: 1, 2, 3.
Với mỗi giá trị của i, vòng lặp bên trong tính toán i * j và tạo một danh sách con.
Chi tiết từng vòng chạy
Lần chạy đầu tiên (i = 1):
Vòng lặp bên trong (for j in range(1, 4)):
Khi j = 1: 1 * 1 = 1.
Khi j = 2: 1 * 2 = 2.
Khi j = 3: 1 * 3 = 3.
Kết quả: [1, 2, 3] (Dòng đầu tiên của ma trận).
Lần chạy thứ hai (i = 2):
Vòng lặp bên trong (for j in range(1, 4)):
Khi j = 1: 2 * 1 = 2.
Khi j = 2: 2 * 2 = 4.
Khi j = 3: 2 * 3 = 6.
Kết quả: [2, 4, 6] (Dòng thứ hai của ma trận).
Lần chạy thứ ba (i = 3):
Vòng lặp bên trong (for j in range(1, 4)):
Khi j = 1: 3 * 1 = 3.
Khi j = 2: 3 * 2 = 6.
Khi j = 3: 3 * 3 = 9.
Kết quả: [3, 6, 9] (Dòng thứ ba của ma trận).
Kết quả cuối cùng
Sau khi hoàn thành cả vòng lặp, matrix trở thành:

python
Sao chép mã
[[1, 2, 3],
 [2, 4, 6],
 [3, 6, 9]]

 2. Xử lý file
Lý thuyết nâng cao
Xử lý file nhị phân: Đọc/ghi file không phải văn bản (ảnh, âm thanh).
Tìm kiếm và thay thế: Đọc file, thay đổi nội dung, và ghi lại.
Tương tác với nhiều file cùng lúc: Mở nhiều file bằng context manager.
Ví dụ nâng cao
Đọc và ghi file nhị phân:
python
Sao chép mã
with open("source.jpg", "rb") as source_file, open("copy.jpg", "wb") as dest_file:
    dest_file.write(source_file.read())
Tìm kiếm và thay thế trong file:
python
Sao chép mã
with open("example.txt", "r") as file:
    content = file.read()

content = content.replace("Python", "JavaScript")

with open("example.txt", "w") as file:
    file.write(content)


3. Ngoại lệ
Lý thuyết nâng cao
Ném ngoại lệ tùy chỉnh: Tự định nghĩa ngoại lệ để quản lý lỗi riêng.
Bắt nhiều loại ngoại lệ: Xử lý nhiều loại lỗi trong cùng một khối try.
Chuỗi ngoại lệ: Dùng raise để tạo chuỗi lỗi.
Ví dụ nâng cao
Định nghĩa ngoại lệ tùy chỉnh:
python
Sao chép mã
class NegativeNumberError(Exception):
    pass

def sqrt(n):
    if n < 0:
        raise NegativeNumberError("Số âm không có căn bậc hai thực.")
    return n ** 0.5

try:
    print(sqrt(-4))
except NegativeNumberError as e:
    print(f"Lỗi: {e}")
Bắt nhiều loại ngoại lệ:
python
Sao chép mã
try:
    x = int(input("Nhập số nguyên: "))
    print(10 / x)
except ValueError:
    print("Đầu vào không hợp lệ.")
except ZeroDivisionError:
    print("Không thể chia cho 0.")

5. Thư viện cần biết
os
Nâng cao: Tương tác với hệ thống tệp và thư mục, kiểm tra quyền truy cập.
python
Sao chép mã
import os

# Kiểm tra quyền truy cập
file_path = "example.txt"
if os.access(file_path, os.R_OK):
    print(f"Có thể đọc file {file_path}")
else:
    print(f"Không thể đọc file {file_path}")

# Tạo thư mục mới
os.makedirs("new_folder", exist_ok=True)
print("Thư mục mới đã được tạo.")
datetime
Nâng cao: Tính toán khoảng thời gian, xử lý múi giờ.
python
Sao chép mã
from datetime import datetime, timedelta

# Thêm 7 ngày vào ngày hiện tại
now = datetime.now()
future_date = now + timedelta(days=7)
print("Ngày hiện tại:", now)
print("Ngày sau 7 ngày:", future_date)
random
Nâng cao: Sinh dữ liệu ngẫu nhiên phức tạp.
python
Sao chép mã
import random

# Sinh mật khẩu ngẫu nhiên
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
password = "".join(random.choices(characters, k=12))
print("Mật khẩu ngẫu nhiên:", password)