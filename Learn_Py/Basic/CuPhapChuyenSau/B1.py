#Sử dụng f-string để format chuỗi, xử lý đầu vào phức tạp hơn.
# Ví dụ: Viết chương trình tính BMI (Body Mass Index) và đưa ra đánh giá sức khỏe.

# Tính BMI = cân nặng (kg) / (chiều cao (m))^2

weight = float(input("Nhập cân nặng của bạn (kg): "))
height = float(input("Nhập chiều cao của bạn (m): "))

bmi = weight / (height ** 2)
if bmi < 18.5:
    status = "gay"
elif 18.5 <= bmi < 24.5:
    status = "binh thuong"
elif 24.5 <= bmi < 29.9:
    status = "thua can"
else: 
    status = "beo phi"
print(f"Chi so BMI cua ban la: {bmi:.1f}. Ban thuoc nhom ({status})")