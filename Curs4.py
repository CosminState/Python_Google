    # liste nu au valori unice

# x = [True, 1, '4']
# print(x[1])
# x[1] = 'a'
# print(x)
# x.append(5)
# print(x)

# x = [1, 3,  2, '3', '4', 5, '6', '7']
# print(x[2][1])
# print(x[1:4])
# print(x[-1])
# print(x[1:2:2])
# print(set(x)) #setul are valori unice, ordoneaza nr
# if 2 in x:
#     print('este')
# print(x.index('4'))


    # set

# x = {1, 3,  2, '3', '4', 5, '6', '7'}
# print(x[2])

    # tuplu => tuple(variabila)
    # set => set(variabila)
    # lista => list(variabila)
    # string => str(variabila)

    # dictionar
        # cheia sa fie unica

# a = {2: '35', 1: '3456'}
# print(a[1])
# a1 = {1: 4}
# a[1] = '222'
# a.update(a1)
# a.update(y=3, b='a')
# print(a)  # are proprietate mutabilitate
# for x in a:
#     print(f'{x} => {a[x]}')

    ##############
    # Selenium Google

from selenium import webdriver
driver = webdriver.Chrome(r'D:\Phyton Curs\Selenium\chromedriver')
driver.maximize_window()
driver.get("https://www.cel.ro/index.php?main_page=login")


def send_text_to_input(name_of_input, text):
    name = driver.find_element_by_name(name_of_input)
    name.send_keys(text)


send_text_to_input('firstname', 'Test')
send_text_to_input('lastname', 'Test')
send_text_to_input('email_address', 'cstate506@gmail.com')
send_text_to_input('telephone', '11180252')
send_text_to_input('street_address', 'Bucuresti')


name = driver.find_element_by_name('termeni')
name.click()
# last_name = driver.find_element_by_name('lastname')
# last_name.send_keys('Test')
















