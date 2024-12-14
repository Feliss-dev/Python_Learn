Run 
pip install -r requirements.txt

4. Sử dụng .env để quản lý biến môi trường
File .env là nơi bạn lưu các thông tin nhạy cảm, chẳng hạn như API keys hoặc secrets.

Ví dụ về .env:

txt
Sao chép mã
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
Cách sử dụng trong chương trình Python: Sử dụng thư viện python-dotenv để đọc file .env:

bash
Sao chép mã
pip install python-dotenv

from dotenv import load_dotenv
import os

# Load biến môi trường từ file .env
load_dotenv()

# Sử dụng biến môi trường
secret_key = os.getenv("SECRET_KEY")
database_url = os.getenv("DATABASE_URL")
print(f"Secret Key: {secret_key}, Database URL: {database_url}")