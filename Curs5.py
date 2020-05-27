# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
#
# req = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')
# response = req.text
# link = BeautifulSoup(response, 'html.parser')
# title = link.find_all('div', attrs={'class': 'contentDiv'})
# """
# <table>
#    <thead>
#        <tr>
#            <th></th>
#            <th></th>
#        </tr>
#    </thead>
#    <tbody>
#        <tr>
#            <td></td>
#            <td></td>
#        </tr>
#        <tr>
#            <td></td>
#            <td></td>
#        </tr>
#    </tbody>
# </table>
# """
# header = []
# data_list = []
# set_td = set()
# header_html = ''
# tbody_html = ''
# td = ''
# tr = ''
# table = ''
# thead = ''
# for i in title:
#     for tr_index in i.find_all('table'):
#         for td_index in tr_index.find_all('tr'):
#             list_td = list()
#             td = ''
#
#             for th_index in td_index.find_all('th'):
#                 header.append(th_index.get_text())
#                 header_html += f'<th>{th_index.get_text()}</th>'
#             thead = f'<thead><tr>{header_html}</tr></thead>'
#             for trd_index in td_index.find_all('td'):
#                 list_td.append(trd_index.get_text().lstrip(' '))
#                 td += f'<td>{trd_index.get_text().lstrip(" ")}</td>'
#             tr += f'<tr>{td}</tr>'
#             data_list.append(tuple(list_td))
# table = f'<table>{thead}<tbody>{tr}</tbody></table>'
# # html
# file = open(r'D:\Python Curs\cursuriScrise\Curs5.html', 'w')
# file.writelines(table)
# file.close()
#
# # Excel
# df = pd.DataFrame(data_list, columns=header)
# df.to_excel('CursBNR_ExcelGoogle.xls', sheet_name='BNR', header=header, index=0)

from selenium import webdriver
import pandas as pd

browser = webdriver.Chrome(r'D:\Python Curs\Selenium\chromedriver')
browser.get('https://www.bnr.ro/files/xml/nbrfxrates2019.htm')
table = browser.find_element_by_xpath('//*[@id="Data_table"]')

# Salvare in txt
# fisier = open('curs_valutar_bnr_google.txt', 'w')
# fisier.writelines(table.text)
# fisier.close()

tabel = table.text
lista = tabel.split('\n')


header_len = browser.find_element_by_xpath('//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')
dictionar = {i: [] for i in header}

for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        if '-' in lista[i]:
            dictionar[header[int(j)]].append(lista[i])
        else:
            dictionar[header[int(j)]].append(float(lista[i]))

import matplotlib.pyplot as plt

# print(dictionar)
df = pd.DataFrame(dictionar)
df.to_excel("BNR_ALL_VALUES_GOOGLE.xls")
browser.close()

# Grafic

a = header[3:9]
c = []
for i in range(3, 9):
    c.append(dictionar[header[int(i)]][int(i)])
d = sum(c)
e = []
for item in c:
    e.append(round(item/d*100))

colors = ['r', 'y', 'g', 'b', 'y', 'g']

plt.pie(e, labels = a, colors = colors, startangle = 90, shadow = True, explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.2), radius = 1.2,
        autopct = '%1.1f%%')
plt.legend()
plt.show()





