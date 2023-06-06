# Задание 4 #Shop: отображение страницы товара товара
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('https://practice.automationtesting.in/')
# driver.find_element_by_link_text('My Account').click()
# id = driver.find_element_by_id
# email_login = id('username')
# email_login.send_keys('L1me4uk@mail.ru')
# password_login = id('password')
# password_login.send_keys('cfnehygkenjy2233')
# driver.find_element_by_css_selector('[name="login"]').click()
# driver.find_element_by_link_text('Shop').click()
# driver.find_element_by_css_selector('[alt="Mastering HTML5 Forms"]').click()
# book_name = driver.find_element_by_css_selector('.summary>h1')
# book_name_text = book_name.text
# assert book_name_text == 'HTML5 Forms'
# driver.quit()



# Задание 5 #Shop: количество товаров в категории категории
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('https://practice.automationtesting.in/')
# driver.find_element_by_link_text('My Account').click()
# id = driver.find_element_by_id
# email_login = id('username')
# email_login.send_keys('L1me4uk@mail.ru')
# password_login = id('password')
# password_login.send_keys('cfnehygkenjy2233')
# driver.find_element_by_css_selector('[name="login"]').click()
# driver.find_element_by_link_text('Shop').click()
# driver.find_element_by_link_text('HTML').click()
# product = driver.find_elements_by_class_name('woocommerce-LoopProduct-link')
# assert len(product) == 3
# driver.quit()

# Задание 6 #Shop: сортировка товаров товаровvalue
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('https://practice.automationtesting.in/')
# driver.find_element_by_link_text('My Account').click()
# id = driver.find_element_by_id
# email_login = id('username')
# email_login.send_keys('L1me4uk@mail.ru')
# password_login = id('password')
# password_login.send_keys('cfnehygkenjy2233')
# driver.find_element_by_css_selector('[name="login"]').click()
# driver.find_element_by_link_text('Shop').click()
# sort = driver.find_element_by_class_name('orderby')
# sort_option = sort.get_attribute('value')
# assert sort_option == 'menu_order'
# select_sort = Select(sort)
# select_sort.select_by_visible_text('Sort by price: high to low')
# sort = driver.find_element_by_class_name('orderby')
# sort_option = sort.get_attribute('value')
# assert sort_option == 'price-desc'
# driver.quit()

# Задание 6 #Shop: отображение, скидка товара товара#
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('https://practice.automationtesting.in/')
# driver.find_element_by_link_text('My Account').click()
# id = driver.find_element_by_id
# email_login = id('username')
# email_login.send_keys('L1me4uk@mail.ru')
# password_login = id('password')
# password_login.send_keys('cfnehygkenjy2233')
# driver.find_element_by_css_selector('[name="login"]').click()
# driver.find_element_by_link_text('Shop').click()
# driver.find_element_by_css_selector('[alt="Android Quick Start Guide"]').click()
# old_price = driver.find_element_by_css_selector('.price del span')
# old_price_text = old_price.text
# new_price = driver.find_element_by_css_selector('.price ins span')
# new_price_text = new_price.text
# print(old_price_text)
# print(new_price_text)
# assert old_price_text == '₹600.00'
# assert new_price_text == '₹450.00'
# wait = WebDriverWait(driver, 10)
# clickable = EC.element_to_be_clickable
# book_img = wait.until(clickable((By.CLASS_NAME, 'images')))
# book_img.click()
# crossfire = wait.until(clickable((By.CLASS_NAME, 'pp_close')))
# crossfire.click()
# driver.quit()


# Задание 7 #Shop: проверка цены в корзине корзине - НЕТ ВОЗМОЖНОСТИ ВЫПОЛНИТЬ ДАЛЬНЕЙШИЕ ЗАДАНИЯ
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('https://practice.automationtesting.in/')
# # id = driver.find_element_by_id
# driver.find_element_by_link_text('Shop').click()