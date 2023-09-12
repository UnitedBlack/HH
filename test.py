import re


def description_parser():
    with open('parserHH.txt', 'r', encoding='utf-8') as file:
        for elem in file:
            # print(line)
            reg_exp_vacancy = r'(.*:\s)(https?:\/\/\S*)'
            match = re.match(reg_exp_vacancy, elem)
            if match:
                vacancy_name, response_url = match.groups()
                print(vacancy_name)

description_parser()

пон норм все чел перерыв на еблю арбуза можно да