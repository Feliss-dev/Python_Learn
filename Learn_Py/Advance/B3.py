# #3. Xử lý dữ liệu với Pandas
# Yêu cầu:
# Đọc file CSV.
# Tính tổng và trung bình của một cột số liệu.

import pandas as pd

#Doc du lieu

data = pd.read_csv("Learn_Py\Advance\data.csv")

#Tinh toan

total = data["Sales"].sum()
average = data["Sales"].mean()

print(f"Tong doanh thu: {total}")