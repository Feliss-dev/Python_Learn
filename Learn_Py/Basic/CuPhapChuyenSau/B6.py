#Ví dụ: Hàm đệ quy tính giai thừa của một số.
def factorial(n):
    if n == 0 or n == 1: # dieu kien dung
        return 1
    return n * factorial(n-1) # goi lai chinh ham do

number = int(input("Nhập một số: "))
print(f"Giai thua cua so {number} la: {factorial(number)}")
