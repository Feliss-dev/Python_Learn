# 1. Lập trình mô phỏng ngân hàng
# Yêu cầu: Tạo lớp BankAccount với các chức năng:
# Gửi tiền (deposit).
# Rút tiền (withdraw).
# Kiểm tra số dư (check_balance).

class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Gui tien thanh cong. So du hien tai: {self.balance}"
    
    def withdraw(self,amount):
        if amount > self.balance:
            return f"So du khong du"
        self.balance -= amount
        return f"Rut tien thanh cong. So du hien tai: {self.balance}"
    
    def check_balance(self):
        return f"So du hien tai: {self.balance}"
    
# Su dung
account = BankAccount("Tran Van A", 100)
print(account.deposit(50))
print(account.withdraw(30))
print(account.check_balance())