# Bài tập 1: Đọc một file văn bản và đếm số dòng, số từ, số ký tự.
with open("D:\B Learn IT on Tube\Python_AI_Project\Python_Learn\Learn_Py\Intermediate\example.txt", "r") as file:
    content = file.read()
    num_lines = len(content.splitlines())
    num_words = len(content.split())
    num_chars = len(content)

print(f"File example.txt góp tốt {num_lines} dòng, {num_words} số, {num_chars} ký tự.")