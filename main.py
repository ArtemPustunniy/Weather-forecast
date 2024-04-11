import requests
import geocoder
import time
name_token = '5aa741a37ff6512516bcb3da3ea973f0'


def my_coords():
    g = geocoder.ip('me')
    latitude = str(g.latlng[0])
    longitude = str(g.latlng[1])
    url_ = 'http://api.openweathermap.org/data/2.5/weather?lat=' + latitude + '&lon=' + longitude + '&units=metric&lang=en&appid=' + name_token
    return url_


def input_coords(lat, lon):
    url_ = 'http://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&units=metric&lang=en&appid=' + name_token
    return url_


def object_coords(object_name):
    url_ = 'http://api.openweathermap.org/data/2.5/weather?q=' + object_name + '&units=metric&lang=ru&appid=' + name_token
    return url_


print('Выберите действие')
print('1. Узнать погоду по моему местоположению')
print('2. Узнать погоду по заданным координатам')
print('3. Узнать погоду по названию географического объекта')
choice = input()
if choice == '1':
    result = requests.get(my_coords()).json()
elif choice == '2':
    latitude = input('Введите широту объекта ')
    longitude = input('Введите долготу объекта ')
    result = requests.get(input_coords(latitude, longitude)).json()
elif choice == '3':
    object_name = input('Введите название объекта ')
    result = requests.get(object_coords(object_name)).json()
else:
    result = requests.get(input_coords('59.85183', '30.15279'))
# print(result)
print(f'Погода в городе {result["name"]}')
print(f'Координаты {result["coord"]["lat"]}, {result["coord"]["lon"]}')
print(f'Дата запроса {time.strftime("%d.%m.%Y", time.localtime())}, время запроса {time.strftime("%H:%M:%S", time.localtime())}')
print(f'Тепература воздуха {result["main"]["temp"]} C')
print(f'Тепература воздуха по ощущениям {result["main"]["feels_like"]} C')
print(f'Давление {result["main"]["pressure"]} мм ртутного столба')




