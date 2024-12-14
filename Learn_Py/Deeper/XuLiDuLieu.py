# #Bài tập thực hành:
# Làm sạch dữ liệu có các giá trị thiếu trong nhiều cột.
# Phân tích doanh số theo sản phẩm và theo khu vực.

import pandas as pd

#Doc file csv
data = pd.read_csv("Learn_Py\Deeper\sales.csv")

#1. Xu li gia tri thieu
data["Sales"].fillna(data["Sales"].mean(), inplace=True) # Điền giá trị trung bình cho cột Sales
data.dropna(subset=["Region"], inplace=True) # Xóa các dòng có giá trị thiếu ở cột Region

#2 Phan tich co ban
print("Tong doanh so:", data["Sales"].sum())
print("Doanh so trung binh:", data["Sales"].mean())

#3 Nhom du lieu
grouped = data.groupby(["Product", "Region"]).sum()
print(grouped)