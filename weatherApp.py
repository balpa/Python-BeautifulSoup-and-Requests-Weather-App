import requests
from bs4 import BeautifulSoup

city = input('Enter the city name: ')
search = 'Weather in {}'.format(city)
url= f'http://www.google.com/search?&q={search}'
req = requests.get(url)
sor = BeautifulSoup(req.text,'html.parser')
temp = sor.find('div',class_='BNeawe').text

print(temp)




