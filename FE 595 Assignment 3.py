import requests
from bs4 import BeautifulSoup

txt_data_male = []
txt_data_female = []

for i in range(0,50):
    get_resp = requests.get("https://www.theyfightcrime.org")
    html = get_resp.content
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

    maleline = soup.find_all('td')
    for male in maleline:
        inner_text = male.text
        strings = inner_text.split(".")
        strings.split('\n')
        first_keyword = 'He'
        second_keyword = 'She'
        txt_data_male.extend([string for string in strings if first_keyword in string])
        txt_data_female.extend([string for string in strings if second_keyword in string])
malefile = open('male.txt', 'w')
malefile.write(tabulate(txt_data_male))
malefile.close()
femalefile = open('female.txt', 'w')
femalefile.write(tabulate(txt_data_female))
femalefile.close()
