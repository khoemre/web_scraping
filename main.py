import requests
from bs4 import BeautifulSoup


url = f'https://www.teknosa.com/laptop-notebook-c-116004'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')




page = soup.find_all(class_='prd')
for i in page:
    marka = i.get('data-product-name').split(' ', 1)
    #print(f'marka: {marka[0]}')
    #print(f'model: {marka[1]}')
    fiyat = i.get('data-product-discounted-price')
    #print(f'fiyat: {fiyat}')

    print(f'Marka: {marka[0]}, Model: {marka[1]}, \nFiyat: {fiyat}')


