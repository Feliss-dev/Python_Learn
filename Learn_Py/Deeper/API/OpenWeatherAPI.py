import requests

API_KEY = "your_api_key"

# Tọa độ của Hà Nội
lat = 446.34  # Vĩ độ
lon = 109.99  # Kinh độ
units = "metric"  # Đơn vị: metric (Celsius), standard (Kelvin), imperial (Fahrenheit)
lang = "enen"


# URL API
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={units}&lang={lang}&appid={API_KEY}"

# Gửi yêu cầu đến API
response = requests.get(url)
if response.status_code == 200:
    weather_data = response.json()
    city_name = weather_data.get("name", "Unknown location")
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    print(f"Nhiệt độ tại {city_name}: {temperature}°C")
    print(f"Thời tiết: {description}")
else:
    print(f"Không thể lấy dữ liệu từ API. Mã lỗi: {response.status_code}")
