import requests
from bs4 import BeautifulSoup
import json
import sqlite3

url = 'https://store.steampowered.com/search/?term=Monomi+Park&hidef2p=1&ndl=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
name_of_game = soup.find_all('span', class_='title')
price = soup.find_all('div', class_='discount_final_price')
some_data = dict()
for i in range(len((name_of_game))):
    print('_______________________')
    print(name_of_game[i].text)
    print(price[i].text)
    
print(some_data)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(some_data,file)

createSQL = """CREATE TABLE name_of_game (name_of_game TEXT, price TEXT)"""
conn = sqlite3.connect('data_from_web.db')
cursor = conn.cursor()
cursor.execute(createSQL)

SQL = """INSERT INTO name_of_game (name_of_game, price) VALUES (?,?)"""

for i in range(len(price)):
    name_of_game = name_of_game[i].text
    price = price[i].text
    cursor.execute(SQL, [name_of_game, price])
    conn.commit()
