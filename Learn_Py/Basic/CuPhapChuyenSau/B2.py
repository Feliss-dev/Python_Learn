#2. Biến và kiểu dữ liệu nâng cao
#Ví dụ: Làm việc với từ điển lồng nhau.
#Viết chương trình quản lý danh sách sinh viên, mỗi sinh viên có thông tin: tên, tuổi, và điểm trung bình.

students = {
    "SV001": {"name": "Nguyen Vaw A", "age": 20, "average_score": 8.5},
    "SV002": {"name": "Trần Thị B", "age": 21, "average_score": 7.2},
    "SV003": {"name": "Lê Văn C", "age": 19, "average_score": 9.0},
}
# In thông tin từng sinh viên
for student_id, info in students.items():
    print(f"ID: {student_id}, Ten: {info['name']}, Tuoi: {info['age']}, Diem TB: {info['average_score']}")

# Tìm sinh viên có điểm trung bình cao nhất
top_student = max(students.items(), key=lambda x: x[1]['average_score'])
print(f"Sinh viên có điểm cao nhất: {top_student[1]['name']} với {top_student[1]['average_score']} điểm.")