# Задание 2 #Registration_login:регистрация аккаунта аккаунта
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('https://practice.automationtesting.in/')
# driver.find_element_by_link_text('My Account').click()
# id = driver.find_element_by_id
# email = id('reg_email')
# email.send_keys('L1me4uk@mail.ru')
# password = id('reg_password')
# password.send_keys('cfnehygkenjy2233')
# driver.find_element_by_css_selector('[name="register"]').click()
# driver.quit()

# Задание 3 #Registration_login:логин в систему
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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
# wait = WebDriverWait(driver, 10)
# wait.until(EC.text_to_be_present_in_element((By.LINK_TEXT, 'Logout'), 'Logout'))
# driver.quit()
