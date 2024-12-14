# #Bài 1: Tải dữ liệu từ 5 API cùng lúc
# Mô tả
# Sử dụng đa luồng để gửi yêu cầu (request) đến 5 API giả lập cùng lúc.
# Mỗi API trả về một kết quả sau một khoảng thời gian.

import threading
import time
import random

#Ham gia lap tai du lieu tu API
def fetch_data(api_id):
    print(f"Starting fetching data from API {api_id}...")
    time.sleep(random.randint(1, 3)) # Giả lập thời gian phản hồi API
    print(f"Data fetching completed for API {api_id}")

#Danh sach API gia lap
api_ids = [1, 2, 3, 4, 5]

#Threads trong
threads = []
for api_id in api_ids:
    thread = threading.Thread(target=fetch_data, args=(api_id,))
    threads.append(thread)
    thread.start()

#Cho den khi tat ca cac luong hoan thanh
for thread in threads:
    thread.join()

#Dấu phẩy (,) trong args=(api_id,) là bắt buộc khi bạn muốn truyền một tuple có một phần tử vào hàm trong Python. Nếu không có dấu phẩy, Python sẽ không nhận diện đó là một tuple mà chỉ là một giá trị đơn lẻ.

# Chi tiết lý do
# Cú pháp của tuple trong Python

# Một tuple trong Python được xác định bằng dấu ngoặc đơn () và các phần tử được phân tách bằng dấu phẩy ,.