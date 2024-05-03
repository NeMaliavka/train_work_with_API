##import requests
##import time
##def find_uk_city(coordinates: list) -> str:
##    # API = '65ae97b123696043220487avude3e26'
##    URL = 'https://geocode.maps.co/reverse?'
##
##    uk_city = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
##
##    for lat, lon in coordinates:
##        response = requests.get(f'{URL}lat={lat}&lon={lon}')
##        try:
##            data = response.json()
##        except:
##           continue
##        
##        city = data['address']['city']
##        #city = data.get('address', {}).get('city')
##        time.sleep(4)
##        if city in uk_city:
##            return city
##
##import requests
##import time
##
##def find_uk_city(coordinates: list) -> str:
##    url = 'https://geocode.maps.co/reverse?'
##    cities = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
##    for lat, lon in coordinates:
##        params = {'lat': lat, 'lon': lon}
##        result = requests.get(url, params=params).json()
##        time.sleep(10)
##        if result['address']['city'] in cities:
##            return result['address']['city']
##
##if __name__ == '__main__':
##    
##    coordinates = [[
##    ('45.4641943', '9.1896346'),
##             ('41.8933203', '12.4829321'),
##             ('51.7520131', '-1.2578499')],
##        [('48.2083537', '16.3725042'),
##        ('52.628606', '1.29227'),
##        ('55.7514952', '37.618153095505875')]
##    ]
##    city = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
##    for i in coordinates:
##        assert find_uk_city(i) in city
##        



##if __name__ == '__main__':
##    _coordinates = [
##        ('48.2083537', '16.3725042'),
##        ('52.628606', '1.29227'),
##        ('55.7514952', '37.618153095505875')
##    ]
##    city = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
##    result = find_uk_city(_coordinates)
##    if result in city:
##        print(result)
##    assert find_uk_city(_coordinates) in city



##n = 10
##i = 1
##while i ** 2 < n:
##    i += 1
##print(i)



# Напишите программу, которая считает неотрицательные
##степени двойки до тех пор, пока это число не станет больше 10 000.
##В ответ запишите количество итераций, которые проделывает цикл.
##num = 1
##i = 0
##while num <= 10000:
##    num *= 2
##    i += 1
##print(i)



# Олег положил тысячу рублей в банк под 8% годовых с ежегодной
##капитализацией процентов. Капитализация процентов означает, что
##проценты за каждый год прибавляются к сумме вклада и в следующем
##году также участвуют в начислении процентов.
##Определите, через сколько лет сумма на счете Олега составит не менее
#трёх тысяч рублей.
##Выведите на экран это число и запишите его в ответ.

p = 8
y = 0
money = 1000
while money <= 3000:
    d = round(money * p / 100)
    money += d
    y += 1
print(money)
print(y)
    





