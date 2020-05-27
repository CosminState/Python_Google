# from selenium import webdriver
# import pandas as pd
#
# browser = webdriver.Chrome(r'D:\Python Curs\Selenium\chromedriver')
# browser.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-22-aprilie-2020-ora-13-00/')
# table = browser.find_element_by_xpath('//*[@id="post-21244"]/div/div/table[1]')
#
# tabel = table.text
# lista = tabel.split('\n')
#
# header_len = browser.find_element_by_xpath('//*[@id="post-21244"]/div/div/table[1]/tbody/tr[1]')
# header = header_len.text.split("\n")
# header_len1 = browser.find_element_by_xpath('//*[@id="post-21244"]/div/div/table[1]/tbody/tr[2]')
# header1 = header_len1.text.split(' ')
# dictionar = {i: [] for i in header1}
# print(header1)
#
# for j in range(0, len(header1)):
#     for i in range(len(header1) + int(j), len(lista), len(header1)):
#         if '.' in lista[i]:
#             dictionar[header1[int(j)]].append(lista[i])
#         else:
#             dictionar[header1[int(j)]].append(float(lista[i]))
#
# df = pd.DataFrame(dictionar)
# df.to_excel("Info_Covid.xls")
# browser.close()
#
# # //*[@id="post-21244"]/div/div/table[1]/tbody/tr[1]/td[1]
# # //*[@id="post-21244"]/div/div/table[1]/tbody/tr[1]/td[2]

import requests
from bs4 import BeautifulSoup
import pandas as pd
total = []
r = requests.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-22-aprilie-2020-ora-13-00/')
s1 = BeautifulSoup(r.text, 'html.parser')
header = '<tr><th>Nr.crt</th><th>Judet</th>'
for i in range(3,25):
    header += f'<th>Aprilie {i}</th>'
header += '</tr>'

rows = ['<tr>' for i in range(43)]

index = 0
for rand in s1.table.findAll('tr')[1:]:
    for crt in rand.findAll('td')[0:1]:  # nr crt
        if index != 42:
            rows[index] += f'<td>{crt.text}</td>'
        else:
            rows[index] += f'<td></td>'

    for jd in rand.findAll('td')[1:2]:  # judet
        if index != 42:
            rows[index] += f'<td>{jd.text}</td>'
        else:
            rows[index] += f'<td>Total</td>'
    index += 1

for zi in range(3, 25):
    index = 0
    url = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-'
    if zi == 7 or zi == 17:
        for i in range(42):
            rows[i] += '<td>Nu exista</td>'
        total.append(f'<td>Nu exista</td>')
    else:
        url += f'{zi}-aprilie-2020-ora-13-00/'
        r = requests.get(url)
        s1 = BeautifulSoup(r.text, 'html.parser')
        for rand in s1.table.findAll('tr')[1:]:
            for camp in rand.findAll('td')[2:]:
                if index != 42:
                    rows[index] += f'<td>{camp.text}</td>'
                index += 1
        if index == 42 or index == 43:
            for rand in s1.table.findAll('tr')[1:]:
                for camp in rand.findAll('td')[1:2]:
                    if '.' in camp.text and 'Mun' not in camp.text or camp.text.isdigit():

                        total.append(f'<td>{camp.text}</td>')


rows[42] += ''.join(total)

for row in rows:
    row += '</tr>'
body = ''.join(rows)
text = f'<table>{header}{body}</table>'
file = open(r'D:\Python Curs\Teme\TemaC5\SituatieCovid.html', 'w', encoding='utf-8')
file.writelines(text)
file.close()

table = pd.read_html(r'D:\Python Curs\Teme\TemaC5\SituatieCovid.html')[0]
table.to_excel(r'D:\Python Curs\Teme\TemaC5\Info_Covid.xls')