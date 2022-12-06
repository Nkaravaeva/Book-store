# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension =r'C:\Users\hp computers\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.2_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver=webdriver.Chrome(chrome_options=chrome_options,executable_path='C:/chromedriver.exe')
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.close()
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://practice.automationtesting.in/")
# driver.find_element_by_id('menu-item-50').click()
# email=driver.find_element_by_id('reg_email')
# email.send_keys('Ivanova@yandex.ru')
# password=driver.find_element_by_id('reg_password')
# password.send_keys('Zvanov212345$!!!!#')
# driver.find_element_by_name('register').click()
# driver.quit()



# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension =r'C:\Users\hp computers\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.3.2_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver=webdriver.Chrome(chrome_options=chrome_options,executable_path='C:/chromedriver.exe')
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.close()
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://practice.automationtesting.in/")
# driver.find_element_by_id('menu-item-50').click()
# email=driver.find_element_by_id('username')
# email.send_keys('Ivanova@yandex.ru')
# password=driver.find_element_by_id('password')
# password.send_keys('Zvanov212345$!!!!#')
# driver.find_element_by_name('login').click()
# element = driver.find_element_by_link_text("Logout")
# element_get_text = element.text
# assert element_get_text=='Logout'
# driver.quit()
