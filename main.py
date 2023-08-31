import requests
import lxml
from bs4 import BeautifulSoup as bs
import re
from forhttp import cookies, headers, params

vacancy = []

response = requests.get('https://hh.ru/search/vacancy',
                        params=params, cookies=cookies, headers=headers)

with open("RequestResult.html", "w", encoding="utf-8") as file:
    file.write(response.text)


soup = bs(response.content, 'html.parser')


title = soup.find_all('a', class_="serp-item__title")

for string in title:
    current_string = string.text
    if current_string:
        regexp = re.search(r"(Python|python|junior python|Junior Python|junior Python|Junior python)", current_string)
        print(regexp)

get_respond_button = soup.find_all(
    class_="bloko-button bloko-button_kind-success bloko-button_scale-small")


# for respond_button in get_respond_button:
#     vacancy.append(respond_button.get("href"))

# print(vacancy)
