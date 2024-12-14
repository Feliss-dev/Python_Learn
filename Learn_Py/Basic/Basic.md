1. Cơ bản (1-2 giờ)
Concepts cần học
Cú pháp Python: print, input, comment.
Biến và kiểu dữ liệu: int, float, str, bool, list, tuple, dict, set.
Cấu trúc điều khiển: if, elif, else.
Vòng lặp: for, while.
Hàm: def, return, các tham số.
Thư viện cần biết
Không cần thêm thư viện.
Bài tập thực hành
Viết chương trình tính tổng và trung bình của danh sách số nguyên nhập từ người dùng.
Viết chương trình kiểm tra số nguyên tố.
Tạo một hàm kiểm tra chuỗi là palindrome hay không.

1. Cú pháp cơ bản
print(): In ra màn hình.
input(): Nhập dữ liệu từ người dùng.
Comment: Dùng dấu # để chú thích.

2. Biến và kiểu dữ liệu
Python hỗ trợ nhiều kiểu dữ liệu cơ bản:

int: Số nguyên
float: Số thực
str: Chuỗi ký tự
bool: Kiểu boolean (True/False)
list: Danh sách
tuple: Bộ dữ liệu không thay đổi
dict: Từ điển (key-value pairs)
set: Tập hợp (không có phần tử trùng lặp)

3. Cấu trúc điều khiển
if, elif, else: Dùng để kiểm tra điều kiện và thực hiện các hành động khác nhau.

4. Vòng lặp
for: Dùng để lặp qua các phần tử trong danh sách, tuple, hoặc dãy số.
while: Dùng để lặp khi điều kiện còn đúng.

5. Hàm
def: Dùng để định nghĩa hàm.
return: Trả về giá trị từ hàm.


Chúng ta sẽ đi qua các khái niệm cơ bản của Python, bao gồm cú pháp, kiểu dữ liệu, cấu trúc điều khiển, vòng lặp, và hàm. Sau đó, tôi sẽ hướng dẫn bạn thực hiện các bài tập thực hành.

1. Cú pháp cơ bản
print(): In ra màn hình.
input(): Nhập dữ liệu từ người dùng.
Comment: Dùng dấu # để chú thích.
python
Sao chép mã
# Đây là một comment, Python sẽ bỏ qua dòng này
print("Hello, World!")  # In ra màn hình
name = input("Nhập tên của bạn: ")  # Nhập dữ liệu từ người dùng
print(f"Chào {name}!")  # In ra lời chào
2. Biến và kiểu dữ liệu
Python hỗ trợ nhiều kiểu dữ liệu cơ bản:

int: Số nguyên
float: Số thực
str: Chuỗi ký tự
bool: Kiểu boolean (True/False)
list: Danh sách
tuple: Bộ dữ liệu không thay đổi
dict: Từ điển (key-value pairs)
set: Tập hợp (không có phần tử trùng lặp)
python
Sao chép mã
x = 10  # int
y = 3.14  # float
name = "Alice"  # str
is_active = True  # bool
numbers = [1, 2, 3, 4]  # list
coordinates = (10, 20)  # tuple
person = {"name": "Alice", "age": 25}  # dict
unique_numbers = {1, 2, 3}  # set
3. Cấu trúc điều khiển
if, elif, else: Dùng để kiểm tra điều kiện và thực hiện các hành động khác nhau.
python
Sao chép mã
age = 18
if age >= 18:
    print("Bạn là người trưởng thành.")
elif age >= 13:
    print("Bạn là thanh thiếu niên.")
else:
    print("Bạn là trẻ em.")
4. Vòng lặp
for: Dùng để lặp qua các phần tử trong danh sách, tuple, hoặc dãy số.
while: Dùng để lặp khi điều kiện còn đúng.
python
Sao chép mã
# Vòng lặp for
for i in range(5):  # Lặp từ 0 đến 4
    print(i)

# Vòng lặp while
count = 0
while count < 5:
    print(count)
    count += 1
5. Hàm
def: Dùng để định nghĩa hàm.
return: Trả về giá trị từ hàm.

**Bài tập thực hành**
**Bài 1**: Tính tổng và trung bình của danh sách số nguyên nhập từ người dùng
Yêu cầu: Viết chương trình yêu cầu người dùng nhập một danh sách các số nguyên và tính tổng và trung bình của các số đó.

**Bài 2**: Kiểm tra số nguyên tố
Yêu cầu: Viết chương trình kiểm tra một số nguyên có phải là số nguyên tố hay không.

**Bài 3**: Kiểm tra chuỗi là palindrome
Yêu cầu: Viết một hàm kiểm tra xem một chuỗi có phải là palindrome (đọc ngược lại vẫn giống nhau) hay không.


Để đào sâu hơn các kiến thức cơ bản, tôi sẽ đưa ra các ví dụ phức tạp hơn, kết hợp nhiều kiến thức trong từng phần.

1. Cú pháp nâng cao
Sử dụng f-string để format chuỗi, xử lý đầu vào phức tạp hơn.

Ví dụ: Viết chương trình tính BMI (Body Mass Index) và đưa ra đánh giá sức khỏe.

2. Biến và kiểu dữ liệu nâng cao
Ví dụ: Làm việc với từ điển lồng nhau.
Viết chương trình quản lý danh sách sinh viên, mỗi sinh viên có thông tin: tên, tuổi, và điểm trung bình.
