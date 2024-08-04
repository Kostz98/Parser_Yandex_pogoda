import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Set-Cookie':'JSESSIONID=51F9D27DBF878175193990C19C6CD14C; Path=/; HttpOnly'
}

url = 'https://yandex.ru/pogoda/moscow?lat=55.755863&lon=37.6177' #чтобы вбить другое место зайдите на https://yandex.ru/pogoda и вбейте в поиске город или район ваш и потом скопируйте ссылку с браузера и втсавте сюда
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

#Ощущаемая температура
feels_like_temp_element = soup.find('div', class_='term__value')
if feels_like_temp_element:
    feels_like_temp = feels_like_temp_element.find('span', class_='temp__value').text
    print(f'Ощущается как: {feels_like_temp}')
else:
    print("Не удалось найти ощущаемую температуру на странице")

# Извлечение влажности
humidity_element = soup.find('div', class_='fact__props').find('div', class_='term term_orient_v fact__humidity').find('div', class_='term__value')
if humidity_element:
    humidity = humidity_element.text.strip()
    print(f'Влажность: {humidity}')
else:
    print("Не удалось найти информацию о влажности")

# Извлечение скорости ветра
wind_speed_element = soup.find('div', class_='fact__props').find('span', class_='wind-speed')
if wind_speed_element:
    wind_speed = wind_speed_element.text.strip()
    print(f'Скорость ветра: {wind_speed} м/с')
else:
    print("Не удалось найти информацию о скорости ветра")
