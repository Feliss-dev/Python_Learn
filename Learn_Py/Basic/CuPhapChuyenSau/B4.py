# #4. Vòng lặp nâng cao
# Ví dụ: Tạo bảng cửu chương từ 1 đến 10.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()
