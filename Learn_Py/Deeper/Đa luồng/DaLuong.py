# #2. Lập trình đa luồng (Threading)
# Khái niệm cơ bản
# Lập trình đa luồng cho phép một chương trình thực hiện nhiều công việc cùng lúc, 
# rất hữu ích khi bạn muốn chạy các tác vụ nặng hoặc xử lý dữ liệu lớn.

import threading
import time

def download_file(file_id):
    print(f"Starting download for file {file_id}")
    time.sleep(2)
    print(f"Download completed for file {file_id}")

# Tao danh sach luong

threads = []
for i in range(5):
    thread = threading.Thread(target=download_file, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()