import requests
import lxml
from bs4 import BeautifulSoup as bs
import re

import requests

cookies = {
    '__ddg1_': 'n7WrjT9BlEJSP38lEdNL',
    '_xsrf': '95db387f997e8c95c556c583dfda82f1',
    'hhrole': 'anonymous',
    'regions': '1',
    'hhtoken': 'OwFtCaikjKfsvhjYySyxwP!ammHq',
    'hhuid': 'm1N2xz2s1fJYI2Tw36syJQ--',
    'crypted_hhuid': 'F967ADE98F26549CB1F9D9BF0B9E4478FDB50D9F272BFFA23AFCCAD89231772E',
    'iap.uid': '7a7cba9619154e228aae717ed0741442',
    '__zzatgib-w-hh': 'MDA0dBA=Fz2+aQ==',
    'display': 'desktop',
    'GMT': '3',
    'redirect_host': 'hh.ru',
    'region_clarified': 'hh.ru',
    'total_searches': '2',
    'cfidsgib-w-hh': 'Brwq++NQIeB3pdX2OqpWtdpJQ6IKXVMY1C8sTUhJBguKC5e3pHJ7l4cJ8SOf9NsKqIXpCViteg+9aA8P/vURe4MTNSpxwHs1BLR3f1uv6jTKQaAfpqeYWLvJbghzCvtsIgWhwGs6ITxCQqYLKUGN5Mvb03EUHdQiDtR0Pw==',
    'cfidsgib-w-hh': 'Brwq++NQIeB3pdX2OqpWtdpJQ6IKXVMY1C8sTUhJBguKC5e3pHJ7l4cJ8SOf9NsKqIXpCViteg+9aA8P/vURe4MTNSpxwHs1BLR3f1uv6jTKQaAfpqeYWLvJbghzCvtsIgWhwGs6ITxCQqYLKUGN5Mvb03EUHdQiDtR0Pw==',
    'gsscgib-w-hh': '7mekXJGnVz9V+4AFAZxc516ogIjFfwSF/m/bozib8OcDR5428lUudE3dBjDLGmUL07+j4tAxBxGhg/NGxsLSU8dXCs5WN8SydMRdgAyr4dVqnhymmXrcnmwvrBgYdYBAoZCG/gO7iNbugfOPB58TGmknhr0w9r1wmfL+Uezb7+BP0Pc6d6BcGOqC6RHcVyJD8ZlTBeXiWVomQ5RJ7O92PMLXkQ4NyutizZ88l6bJ1eKW91J6J5zMy+TDMy+dIw==',
    'device_magritte_breakpoint': 'l',
    'device_breakpoint': 'm',
    'fgsscgib-w-hh': 'CSyld6c023127ef31cfb7227071ceab8c9c19dec',
}

headers = {
    'authority': 'hh.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '__ddg1_=n7WrjT9BlEJSP38lEdNL; _xsrf=95db387f997e8c95c556c583dfda82f1; hhrole=anonymous; regions=1; hhtoken=OwFtCaikjKfsvhjYySyxwP!ammHq; hhuid=m1N2xz2s1fJYI2Tw36syJQ--; crypted_hhuid=F967ADE98F26549CB1F9D9BF0B9E4478FDB50D9F272BFFA23AFCCAD89231772E; iap.uid=7a7cba9619154e228aae717ed0741442; __zzatgib-w-hh=MDA0dBA=Fz2+aQ==; display=desktop; GMT=3; redirect_host=hh.ru; region_clarified=hh.ru; total_searches=2; cfidsgib-w-hh=Brwq++NQIeB3pdX2OqpWtdpJQ6IKXVMY1C8sTUhJBguKC5e3pHJ7l4cJ8SOf9NsKqIXpCViteg+9aA8P/vURe4MTNSpxwHs1BLR3f1uv6jTKQaAfpqeYWLvJbghzCvtsIgWhwGs6ITxCQqYLKUGN5Mvb03EUHdQiDtR0Pw==; cfidsgib-w-hh=Brwq++NQIeB3pdX2OqpWtdpJQ6IKXVMY1C8sTUhJBguKC5e3pHJ7l4cJ8SOf9NsKqIXpCViteg+9aA8P/vURe4MTNSpxwHs1BLR3f1uv6jTKQaAfpqeYWLvJbghzCvtsIgWhwGs6ITxCQqYLKUGN5Mvb03EUHdQiDtR0Pw==; gsscgib-w-hh=7mekXJGnVz9V+4AFAZxc516ogIjFfwSF/m/bozib8OcDR5428lUudE3dBjDLGmUL07+j4tAxBxGhg/NGxsLSU8dXCs5WN8SydMRdgAyr4dVqnhymmXrcnmwvrBgYdYBAoZCG/gO7iNbugfOPB58TGmknhr0w9r1wmfL+Uezb7+BP0Pc6d6BcGOqC6RHcVyJD8ZlTBeXiWVomQ5RJ7O92PMLXkQ4NyutizZ88l6bJ1eKW91J6J5zMy+TDMy+dIw==; device_magritte_breakpoint=l; device_breakpoint=m; fgsscgib-w-hh=CSyld6c023127ef31cfb7227071ceab8c9c19dec',
    'referer': 'https://hh.ru/?customDomain=1',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

params = {
    'area': '1',
    'experience': 'noExperience',
    'search_field': [
        'name',
        'company_name',
        'description',
    ],
    'text': 'Python junior',
    'enable_snippets': 'false',
    'L_save_area': 'true',
}

response = requests.get('https://hh.ru/search/vacancy',
                        params=params, cookies=cookies, headers=headers)

with open("RequestResult.html", "w", encoding="utf-8") as file:
    file.write(response.text)

soup = bs(response.content, 'html.parser')

title = soup.find_all('a', class_="serp-item__title")
respond_button = soup.find_all(
    class_="bloko-button bloko-button_kind-success bloko-button_scale-small").find("span")
print(respond_button)
