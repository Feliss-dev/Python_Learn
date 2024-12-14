# Bài 3: Chương trình kiểm tra một chuỗi có phải là palindrome không.
#  Một chuỗi là palindrome nếu nó đọc từ trái sang phải và từ phải sang trái giống nhau. 
# Chúng ta loại bỏ khoảng trắng và chuyển chuỗi thành chữ thường để kiểm tra.
def is_palindrome(s):
    s  = s.replace(" ", "").lower() # Loai bo khoang trang va chuyen ve chu thuong
    return s == s[::-1] # So sanh xau goc voi xau dao nguoc

word = input("Nhap 1 chuoi:")
if is_palindrome(word):
    print(f"{word} la chuoi doi xung")
else:
    print(f"{word} khong phai la chuoi doi xung")