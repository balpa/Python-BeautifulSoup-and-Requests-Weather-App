# @author: Berke Altıparmak
# You may use, distribute and modify this code under the
# terms of the Beerware license, which unfortunately won't be
# written for another century.
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <berkealtiparmak@outlook.com> wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.   Berke Altıparmak
# ----------------------------------------------------------------------------
#


import requests
from bs4 import BeautifulSoup

city = input('Enter the city name: ')
search = 'Weather in {}'.format(city)
url= f'http://www.google.com/search?&q={search}'
req = requests.get(url)
sor = BeautifulSoup(req.text,'html.parser')
temp = sor.find('div',class_='BNeawe').text

print(temp)




