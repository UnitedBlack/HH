from bs4 import BeautifulSoup
import requests
from forhttp import cookies, headers, params
from lxml import etree

import requests

# cookies = {
#     '_xsrf': '40dd8a4e45483d8ff41a7d36d7d5e12e',
#     'regions': '1',
#     'display': 'desktop',
#     'hhtoken': 'jdLjYoVcbug_xOfXz!_H5YDtxWP2',
#     'hhuid': 'YRCmSQVhvI1ot2MSrbwuRQ--',
#     'GMT': '3',
#     'iap.uid': '3ee62c4778fc4b95821f05feaad7eba5',
#     'crypted_hhuid': '92E8CA641EDF89BE51BEA1CE6EC77503EEFF509069FFA31986D500E6E8923AC7',
#     'hhul': '861db128a244446be64b9f1e0c8d9cbc2573e584aa91f9e4f9d3e994106bd774',
#     '_ym_uid': '1665671495555626923',
#     '__zzatundefined': 'MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS9BKyxcbCMeYUcXVEgRUzNaG0Y1bikLCEBhcEEpcy9waSBjTlojRlZWayELUTQ1ZhBKT01HMzg/aH0eVBw5VREPFhI2FyMSfXIkTwgRXEJHdXsqN1dhMA8WEU1HDTJoUXtMZxUTRkIce3AtLGxzVycyOSdQfyIKay8LEntwKlEMD2RBM2llaXAvYCASJRFNRxhFZFtCNigVS3FPHHp2X30qQWweX0hfIEhbVn4lFXtDPGMMcRVNCA03QFx/V2pbORdYCRQKQ2VbSj03FVlSdSlufTowG0VXUh1MYVRED1U2LiEYMXQjUg8SYz51cHkubyAmG0pgJXRHSWtlTlNCLGYbcRVNCA00PVpyIg9bOSVYCBI/CyYfGHhrJFUIEGFGRnBvG382XRw5YxEOIRdGWF17TEA=Ickg7Q==',
#     '__ddgid_': 'NgxmP9kvO9Pm4tsv',
#     '_ym_d': '1681835512',
#     '_ga_44H5WGZ123': 'GS1.1.4aef11d6ade11cd2cf38573399c63a5bfb70ea8a8d6b721203f82d9cf779726b.246.1.1682465230.60.0.0',
#     '_ga': 'GA1.2.1704764943.1668101831',
#     'subscription_informer_declined': 'true',
#     '__zzatgib-w-hh': 'MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS9BKyxcbCMeYUcXVEgRUzNaG0Y1bikLCEBhcEEpcy9waSBjTlojRlZWayELUTQ1ZhBKT01HMzg/aH0eVBw5VREPFhI2FyMSfXMqWAwTXUJIc3cvN1dhMA8WEU1HDTJoUXtMZxUTRkIce3AtLGxzVycyOSdQfyIKay8LEntwKlEMD2RBM2llaXAvYCASJRFNRxhFZFtCNigVS3FPHHp2X30qQW0kaExhIUhcU34lFXtDPGMMcRVNCA03QFx/V2pbORdYCRQKQ2VbSj03FVlSdSlufTowG0VXUBpLFVR1WFA2WBkTMCdZUQsUXUNGdjEwcSEiZ3gWIUpHSWtlTlNCLGYbcRVNCA00PVpyIg9bOSVYCBI/CyYfGX50KFcJEGJDR3VvG382XRw5YxEOIRdGWF17TEA=HT8hXQ==',
#     'hhrole': 'anonymous',
#     '__ddg1_': 'CU17BmF70FPpDANhcuUm',
#     'region_clarified': 'NOT_SET',
#     '_ym_isad': '2',
#     '_gid': 'GA1.2.1717738298.1694203522',
#     '_gat_gtag_UA_11659974_2_DG': '1',
#     '_ym_visorc': 'w',
#     'cfidsgib-w-hh': 'hKhgH8cuvWrvPRnERnIvMAE/JdnAqH6I08Gv8JILTBSSItqLwEB4MyiJditLvYLfkMB/wmKP6QFXg4YpPSSgcJ4gKDQFRtJ7R3/MHATPAAps0XJZIljJEcnnvMheIX5RMRYVQTOw64SS6nhqSFtC+62CqdN7dQuTYV+sz9q60A==',
#     'cfidsgib-w-hh': 'hKhgH8cuvWrvPRnERnIvMAE/JdnAqH6I08Gv8JILTBSSItqLwEB4MyiJditLvYLfkMB/wmKP6QFXg4YpPSSgcJ4gKDQFRtJ7R3/MHATPAAps0XJZIljJEcnnvMheIX5RMRYVQTOw64SS6nhqSFtC+62CqdN7dQuTYV+sz9q60A==',
#     'gsscgib-w-hh': 'CUL4g31tf34BTyYcpwW0f70reBvVBs5xvrXWHSk+CRe5BCWKB/V8duG4O4ofXJ6QaK1G7Cmjs5tBJnAp1erqlzVSMfaF7GKuneK4ms13eipBSzSCHTIbxN1Is4uj4iAKgWOMrgCbj8ubFyX1ceO9c3FxiC+V+yllEqCT4MfK3O5va6QhOxyGjV0v9yYQyCLlHLBC9qBHGCw10oNqhBStEJfiQTTTJlWfGpR/yCrT41w8KuUl13CeVis5ySh6Dg==',
#     'device_magritte_breakpoint': 's',
#     'device_breakpoint': 's',
#     'total_searches': '4',
#     'fgsscgib-w-hh': 'cDqW4a0c91971abdf7f9333cc85b27c026844e2f',
# }

# headers = {
#     'authority': 'hh.ru',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'cache-control': 'max-age=0',
#     # 'cookie': '_xsrf=40dd8a4e45483d8ff41a7d36d7d5e12e; regions=1; display=desktop; hhtoken=jdLjYoVcbug_xOfXz!_H5YDtxWP2; hhuid=YRCmSQVhvI1ot2MSrbwuRQ--; GMT=3; iap.uid=3ee62c4778fc4b95821f05feaad7eba5; crypted_hhuid=92E8CA641EDF89BE51BEA1CE6EC77503EEFF509069FFA31986D500E6E8923AC7; hhul=861db128a244446be64b9f1e0c8d9cbc2573e584aa91f9e4f9d3e994106bd774; _ym_uid=1665671495555626923; __zzatundefined=MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS9BKyxcbCMeYUcXVEgRUzNaG0Y1bikLCEBhcEEpcy9waSBjTlojRlZWayELUTQ1ZhBKT01HMzg/aH0eVBw5VREPFhI2FyMSfXIkTwgRXEJHdXsqN1dhMA8WEU1HDTJoUXtMZxUTRkIce3AtLGxzVycyOSdQfyIKay8LEntwKlEMD2RBM2llaXAvYCASJRFNRxhFZFtCNigVS3FPHHp2X30qQWweX0hfIEhbVn4lFXtDPGMMcRVNCA03QFx/V2pbORdYCRQKQ2VbSj03FVlSdSlufTowG0VXUh1MYVRED1U2LiEYMXQjUg8SYz51cHkubyAmG0pgJXRHSWtlTlNCLGYbcRVNCA00PVpyIg9bOSVYCBI/CyYfGHhrJFUIEGFGRnBvG382XRw5YxEOIRdGWF17TEA=Ickg7Q==; __ddgid_=NgxmP9kvO9Pm4tsv; _ym_d=1681835512; _ga_44H5WGZ123=GS1.1.4aef11d6ade11cd2cf38573399c63a5bfb70ea8a8d6b721203f82d9cf779726b.246.1.1682465230.60.0.0; _ga=GA1.2.1704764943.1668101831; subscription_informer_declined=true; __zzatgib-w-hh=MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS9BKyxcbCMeYUcXVEgRUzNaG0Y1bikLCEBhcEEpcy9waSBjTlojRlZWayELUTQ1ZhBKT01HMzg/aH0eVBw5VREPFhI2FyMSfXMqWAwTXUJIc3cvN1dhMA8WEU1HDTJoUXtMZxUTRkIce3AtLGxzVycyOSdQfyIKay8LEntwKlEMD2RBM2llaXAvYCASJRFNRxhFZFtCNigVS3FPHHp2X30qQW0kaExhIUhcU34lFXtDPGMMcRVNCA03QFx/V2pbORdYCRQKQ2VbSj03FVlSdSlufTowG0VXUBpLFVR1WFA2WBkTMCdZUQsUXUNGdjEwcSEiZ3gWIUpHSWtlTlNCLGYbcRVNCA00PVpyIg9bOSVYCBI/CyYfGX50KFcJEGJDR3VvG382XRw5YxEOIRdGWF17TEA=HT8hXQ==; hhrole=anonymous; __ddg1_=CU17BmF70FPpDANhcuUm; region_clarified=NOT_SET; _ym_isad=2; _gid=GA1.2.1717738298.1694203522; _gat_gtag_UA_11659974_2_DG=1; _ym_visorc=w; cfidsgib-w-hh=hKhgH8cuvWrvPRnERnIvMAE/JdnAqH6I08Gv8JILTBSSItqLwEB4MyiJditLvYLfkMB/wmKP6QFXg4YpPSSgcJ4gKDQFRtJ7R3/MHATPAAps0XJZIljJEcnnvMheIX5RMRYVQTOw64SS6nhqSFtC+62CqdN7dQuTYV+sz9q60A==; cfidsgib-w-hh=hKhgH8cuvWrvPRnERnIvMAE/JdnAqH6I08Gv8JILTBSSItqLwEB4MyiJditLvYLfkMB/wmKP6QFXg4YpPSSgcJ4gKDQFRtJ7R3/MHATPAAps0XJZIljJEcnnvMheIX5RMRYVQTOw64SS6nhqSFtC+62CqdN7dQuTYV+sz9q60A==; gsscgib-w-hh=CUL4g31tf34BTyYcpwW0f70reBvVBs5xvrXWHSk+CRe5BCWKB/V8duG4O4ofXJ6QaK1G7Cmjs5tBJnAp1erqlzVSMfaF7GKuneK4ms13eipBSzSCHTIbxN1Is4uj4iAKgWOMrgCbj8ubFyX1ceO9c3FxiC+V+yllEqCT4MfK3O5va6QhOxyGjV0v9yYQyCLlHLBC9qBHGCw10oNqhBStEJfiQTTTJlWfGpR/yCrT41w8KuUl13CeVis5ySh6Dg==; device_magritte_breakpoint=s; device_breakpoint=s; total_searches=4; fgsscgib-w-hh=cDqW4a0c91971abdf7f9333cc85b27c026844e2f',
#     'referer': 'https://hh.ru/search/vacancy?area=1&employment=full&employment=part&employment=probation&excluded_text=%D0%BC%D0%B0%D1%80%D0%BA%D0%B5%D1%82%D0%BF%D0%BB%D0%B5%D0%B9%D1%81%D1%8B+%D0%B2%D0%B0%D0%B9%D0%BB%D0%B4%D0%B1%D0%B5%D1%80%D0%B8%D1%81+%D0%BE%D0%B7%D0%BE%D0%BD+%D0%BD%D0%B5%D0%B4%D0%B2%D0%B8%D0%B6%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%8C+%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0&experience=noExperience&industry=7.541&industry=7.539&industry=11.459&industry=44.393&professional_role=170&professional_role=2&professional_role=3&professional_role=37&professional_role=163&professional_role=68&schedule=fullDay&schedule=shift&schedule=flexible&search_field=name&search_field=company_name&search_field=description&clusters=true&enable_snippets=true&no_magic=true&ored_clusters=true&order_by=salary_asc&page=1&hhtmFrom=vacancy_search_list',
#     'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0',
# }

# params = {
#     'area': '1',
#     'employment': [
#         'full',
#         'part',
#         'probation',
#     ],
#     'excluded_text': 'маркетплейсы вайлдберис озон недвижимость стройка',
#     'experience': 'noExperience',
#     'industry': [
#         '7.541',
#         '7.539',
#         '11.459',
#         '44.393',
#     ],
#     'professional_role': [
#         '170',
#         '2',
#         '3',
#         '37',
#         '163',
#         '68',
#     ],
#     'schedule': [
#         'fullDay',
#         'shift',
#         'flexible',
#     ],
#     'search_field': [
#         'name',
#         'company_name',
#         'description',
#     ],
#     'clusters': 'true',
#     'enable_snippets': 'true',
#     'no_magic': 'true',
#     'ored_clusters': 'true',
#     'order_by': 'salary_asc',
#     'page': '0',
# }

# response = requests.get('https://hh.ru/search/vacancy', params=params, cookies=cookies, headers=headers)


# url = "https://hh.ru/search/vacancy?area=1&employment=probation&experience=noExperience&professional_role=163&professional_role=68&professional_role=170&professional_role=150&professional_role=107&search_field=name&search_field=company_name&search_field=description&enable_snippets=true&text=&no_magic=true&L_save_area=true&items_on_page=50&page=0"

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0"
# }

# req = requests.get(url, headers = headers)
# src = req.text

# print(src)

# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)

# with open("index1.html", "w", encoding="utf-8") as file:
#     file.write(response.text)


with open("index1.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
xml_doc = src
all_vacancies_hrefs = soup.find_all(class_="serp-item__title")
# all_vacancies_hrefs = soup.select(".serp-item__title")
# all_vacancies_hrefs = soup.find(class_="serp-item").find("span").find_all("a")

# all_vacancies_hrefs = soup.find_all('h3')

# print(all_vacancies_hrefs)
print(len(all_vacancies_hrefs))

# for i, item in enumerate(all_vacancies_hrefs):
#      item_text = item.text
#      item_href = item.get("href")
#      print(f"{i+1}. {item_text}: {item_href}")
