# Ví dụ: Hàm xử lý danh sách sinh viên với nhiều tính năng.

students = [
    {"name": "Nguyen Van A", "score": 8.5},
    {"name": "Tran Thi B", "score": 7.2},
    {"name": "Le Van C", "score": 9.0},
]
print(type(students))

def get_average_score(students):
    return sum(students['score'] for students in students) / len(students)

def find_top_student(students):
    return max(students, key=lambda x: x["score"])

#Tinh diem trung binh 
average_score = get_average_score(students)
print(f"Diem trung binh cua lop la: {average_score}")

#Tim sinh vien co diem cao nhat
top_student = find_top_student(students)
print(f"Sinh vien co diem cao nhat la: {top_student['name']}")
