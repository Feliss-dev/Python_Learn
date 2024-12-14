1. OOP (Lập trình hướng đối tượng)
Khái niệm cơ bản
Class (Lớp): Là một khuôn mẫu để tạo ra các đối tượng. Nó chứa thuộc tính (biến) và phương thức (hàm).
Object (Đối tượng): Là một thực thể của lớp, đại diện cho một vật thể cụ thể.
__init__: Là hàm khởi tạo, được gọi tự động khi tạo một đối tượng từ lớp.
Ví dụ:

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name  # Thuộc tính
        self.balance = balance

    def deposit(self, amount):  # Phương thức
        self.balance += amount
        return f"{self.name} đã gửi {amount}. Số dư hiện tại: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return f"Số dư không đủ!"
        self.balance -= amount
        return f"{self.name} đã rút {amount}. Số dư hiện tại: {self.balance}"

Kế thừa (Inheritance)
Cho phép một lớp con kế thừa thuộc tính và phương thức từ lớp cha.

class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.05):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        return f"Lãi suất đã được áp dụng. Số dư hiện tại: {self.balance}"


Hướng dẫn chi tiết lý thuyết và các dạng bài tập nâng cao
1. OOP (Lập trình hướng đối tượng)
Khái niệm cơ bản
Class (Lớp): Là một khuôn mẫu để tạo ra các đối tượng. Nó chứa thuộc tính (biến) và phương thức (hàm).
Object (Đối tượng): Là một thực thể của lớp, đại diện cho một vật thể cụ thể.
__init__: Là hàm khởi tạo, được gọi tự động khi tạo một đối tượng từ lớp.
Ví dụ:
python
Sao chép mã
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name  # Thuộc tính
        self.balance = balance

    def deposit(self, amount):  # Phương thức
        self.balance += amount
        return f"{self.name} đã gửi {amount}. Số dư hiện tại: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return f"Số dư không đủ!"
        self.balance -= amount
        return f"{self.name} đã rút {amount}. Số dư hiện tại: {self.balance}"
Kế thừa (Inheritance)
Cho phép một lớp con kế thừa thuộc tính và phương thức từ lớp cha.
python
Sao chép mã
class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.05):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        return f"Lãi suất đã được áp dụng. Số dư hiện tại: {self.balance}"
Decorators
Là gì? Decorators là hàm dùng để tùy chỉnh hoặc mở rộng hành vi của hàm khác mà không thay đổi trực tiếp hàm đó.
Cú pháp: Dùng @decorator_name ngay trên hàm cần tùy chỉnh.

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Hàm {func.__name__} được gọi với các tham số {args}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(3, 5))


Hướng dẫn chi tiết lý thuyết và các dạng bài tập nâng cao
1. OOP (Lập trình hướng đối tượng)
Khái niệm cơ bản
Class (Lớp): Là một khuôn mẫu để tạo ra các đối tượng. Nó chứa thuộc tính (biến) và phương thức (hàm).
Object (Đối tượng): Là một thực thể của lớp, đại diện cho một vật thể cụ thể.
__init__: Là hàm khởi tạo, được gọi tự động khi tạo một đối tượng từ lớp.
Ví dụ:
python
Sao chép mã
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name  # Thuộc tính
        self.balance = balance

    def deposit(self, amount):  # Phương thức
        self.balance += amount
        return f"{self.name} đã gửi {amount}. Số dư hiện tại: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return f"Số dư không đủ!"
        self.balance -= amount
        return f"{self.name} đã rút {amount}. Số dư hiện tại: {self.balance}"
Kế thừa (Inheritance)
Cho phép một lớp con kế thừa thuộc tính và phương thức từ lớp cha.
python
Sao chép mã
class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.05):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        return f"Lãi suất đã được áp dụng. Số dư hiện tại: {self.balance}"

1. OOP (Lập trình hướng đối tượng)
Các khái niệm nâng cao
1.1. Tính đóng gói (Encapsulation)
Mục đích: Giúp bảo vệ dữ liệu bằng cách ẩn các thuộc tính bên trong lớp, chỉ cho phép truy cập qua phương thức.
Cách thực hiện: Dùng tiền tố _ (protected) hoặc __ (private).
python
Sao chép mã

class SecureBankAccount:
    def __init__(self, name, balance=0):
        self.__name = name          # Thuộc tính private
        self.__balance = balance    # Thuộc tính private

    def deposit(self, amount):
        self.__balance += amount
        return f"Gửi thành công, số dư: {self.__balance}"

    def __log_transaction(self):  # Phương thức private
        print("Giao dịch được ghi nhận.")

account = SecureBankAccount("Nguyễn Văn A", 1000)
print(account.deposit(500))
# print(account.__balance)  # Lỗi vì __balance là private

1.2. Tính kế thừa nâng cao
Khi kế thừa, ta có thể:
Ghi đè phương thức (method overriding): Lớp con thay đổi hành vi của phương thức lớp cha.
Gọi phương thức lớp cha bằng super().

class BankAccount:
    def withdraw(self, amount):
        return f"Rút {amount}"

class SecureBankAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 1000:
            return "Rút tiền thất bại: Vượt quá hạn mức."
        return super().withdraw(amount)

acc = SecureBankAccount()
print(acc.withdraw(1500))  # Gọi phương thức ghi đè
print(acc.withdraw(500))   # Gọi phương thức lớp cha qua super()

1.3. Tính đa hình (Polymorphism)
Khái niệm: Một phương thức có thể hoạt động khác nhau trên các lớp khác nhau.

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(3, 4), Circle(5)]
for shape in shapes:
    print(shape.area())
1.4. Các phương thức đặc biệt (dunder methods)
Dùng để: Tùy chỉnh hành vi các toán tử và hàm mặc định.
Ví dụ: __str__, __add__, __len__.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Ghi đè toán tử cộng
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):  # Hiển thị dạng chuỗi
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)
print(v1 + v2)  # Vector(3, 7)


Decorators
Là gì? Decorators là hàm dùng để tùy chỉnh hoặc mở rộng hành vi của hàm khác mà không thay đổi trực tiếp hàm đó.
Cú pháp: Dùng @decorator_name ngay trên hàm cần tùy chỉnh.
python
Sao chép mã
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Hàm {func.__name__} được gọi với các tham số {args}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(3, 5))
Generator
Là gì? Generator là cách tạo iterator hiệu quả bằng cách sử dụng từ khóa yield.
Tại sao dùng? Tiết kiệm bộ nhớ hơn so với tạo danh sách lớn.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib = fibonacci(10)
print(list(fib))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

2.1. Generator Expressions
Dùng để: Tạo generator nhanh gọn thay vì định nghĩa hàm.

gen = (x**2 for x in range(5))
print(next(gen))  # 0
print(next(gen))  # 1


Pandas
Dùng để: Xử lý dữ liệu dạng bảng.
Các thao tác cơ bản:
Đọc file CSV: pd.read_csv("file.csv")
Tính toán trên cột: .sum(), .mean(), .max()

import pandas as pd

# Đọc file CSV
data = pd.read_csv("data.csv")

# Tính tổng và trung bình của cột "Sales"
total_sales = data["Sales"].sum()
average_sales = data["Sales"].mean()

print(f"Tổng doanh thu: {total_sales}, Doanh thu trung bình: {average_sales}")

Matplotlib
Dùng để: Vẽ biểu đồ và trực quan hóa dữ liệu.

import matplotlib.pyplot as plt

# Dữ liệu
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Vẽ biểu đồ
plt.plot(x, y, label="Sales", color="blue")
plt.xlabel("Time")
plt.ylabel("Revenue")
plt.title("Revenue Over Time")
plt.legend()
plt.show()


NumPy
Dùng để: Xử lý mảng số học hiệu quả.
import numpy as np

# Tạo mảng NumPy
arr = np.array([1, 2, 3, 4, 5])

# Các phép toán
print("Tổng:", np.sum(arr))
print("Trung bình:", np.mean(arr))
print("Mảng bình phương:", np.square(arr))
