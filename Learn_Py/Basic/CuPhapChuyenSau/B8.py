 #6. Kết hợp các kiến thức cơ bản
# Bài toán tổng hợp: Quản lý một danh sách sản phẩm.
# Viết chương trình quản lý danh sách sản phẩm, mỗi sản phẩm có:

# Tên sản phẩm
# Giá
# Số lượng tồn kho
# Chương trình cho phép:

# Thêm sản phẩm mới.
# Cập nhật số lượng tồn kho.
# Tính tổng giá trị tồn kho.

products = {}

def add_product(name, price, quantity):
    products[name] = {'price': price, 'quantity': quantity}

def update_quantity(name, quantity):
    if name in products:
        products[name]["quantity"] += quantity
    else:
        print(f"Không tìm thấy sản phẩm {name}")

def calculate_total_value():
    return sum(info["price"] * info["quantity"] for info in products.values())

# Thêm sản phẩm
add_product("Bút", 5000, 100)
add_product("Sách", 20000, 50)
add_product("Tẩy", 3000, 200)

# Cập nhật số lượng tồn kho
update_quantity("Bút", 50)
update_quantity("Sách", -10)

# Tính tổng giá trị tồn kho
total_value = calculate_total_value()
print(f"Tổng giá trị tồn kho: {total_value} VND")