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
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_link_text('HTML').click()
# count= driver.find_element_by_css_selector(".cat-item-19 >span")
# element_get_text = count.text
# assert element_get_text=="(3)"
# driver.quit()


# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
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
# driver.find_element_by_id('menu-item-40').click()
# default_sorting= driver.find_element_by_name('orderby')
# default_sorting_check = default_sorting.get_attribute("value")
# if default_sorting_check == "menu_order":
#     print("Default sorting")
# else:
#     print("False")
# high_to_low= driver.find_element_by_name("orderby")
# select = Select(high_to_low)  # Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
# select.select_by_value("price-desc")  # ищем элемент с текстом "Sales" ; в этом и предыдущем методе добавлять .click() не нужно
# high_to_low= driver.find_element_by_name("orderby")
# high_to_low_check = high_to_low.get_attribute("value")
# if high_to_low_check == "price-desc":
#     print("Sort by price: high to low")
# else:
#     print("False")
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
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_css_selector('.post-181').click()
# element = driver.find_element_by_css_selector('.entry-title')
# element_get_text = element.text
# assert element_get_text=="HTML5 Forms"
# driver.quit()



# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_css_selector('.post-169').click()
# old_price= driver.find_element_by_css_selector('p>del>span')
# old_price_get_text = old_price.text
# assert old_price_get_text=="₹600.00"
# new_price= driver.find_element_by_css_selector('p>ins>span')
# new_price_get_text = new_price.text
# assert new_price_get_text=="₹450.00"
# book_cover=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
# book_close=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# book_close.click()
# driver.quit()


# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_css_selector('.post-182>.button').click()
# time.sleep(3)
# items= driver.find_element_by_css_selector('.cartcontents')
# items_get_text = items.text
# assert items_get_text == "1 Item"
# price= driver.find_element_by_css_selector('.wpmenucart-contents>span.amount')
# price_get_text = price.text
# assert price_get_text=="₹180.00"
# driver.find_element_by_id('wpmenucartli').click()
# subtotal_price = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal>td"), "₹180.00"))
# total_price= WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total>td"), "₹183.60"))
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
# driver.find_element_by_id('menu-item-40').click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_css_selector('.post-182>.button').click()
# time.sleep(3)
# driver.find_element_by_css_selector('.post-180>.button').click()
# time.sleep(3)
# driver.find_element_by_id('wpmenucartli').click()
# time.sleep(3)
# driver.find_element_by_css_selector('a.remove').click()
# driver.find_element_by_css_selector('.woocommerce-message>a').click()
# quantity=driver.find_element_by_css_selector('.quantity>input')
# quantity.clear()
# quantity.send_keys('3')
# driver.find_element_by_name('update_cart').click()
# quantity_check = quantity.get_attribute("value")
# assert quantity_check == "3"
# time.sleep(5)
# driver.find_element_by_name('apply_coupon').click()
# message=driver.find_element_by_css_selector('.woocommerce-error>li')
# message_get_text = message.text
# assert message_get_text == "Please enter a coupon code."
# driver.quit()



# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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
# driver.find_element_by_id('menu-item-40').click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_css_selector('.post-182>.button').click()
# time.sleep(3)
# driver.find_element_by_id('wpmenucartli').click()
# time.sleep(3)
# driver.find_element_by_css_selector('.wc-forward').click()
# first_name=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"billing_first_name")))
# first_name.send_keys('Ivan')
# last_name=driver.find_element_by_id('billing_last_name')
# last_name.send_keys('Ivanov')
# email=driver.find_element_by_id('billing_email')
# email.send_keys('ivanov@yandex.ru')
# phone=driver.find_element_by_id('billing_phone')
# phone.send_keys('+7925325565')
# driver.find_element_by_id('select2-chosen-1').click()
# search=driver.find_element_by_id('s2id_autogen1_search')
# search.send_keys('Russia')
# driver.find_element_by_id('select2-results-1').click()
# adress_1=driver.find_element_by_id('billing_address_1')
# adress_1.send_keys('Lenina')
# adress_2=driver.find_element_by_id('billing_address_2')
# adress_2.send_keys('3')
# city=driver.find_element_by_id('billing_city')
# city.send_keys('Moscow')
# state=driver.find_element_by_id('billing_state')
# state.send_keys('Moscow')
# postcode=driver.find_element_by_id('billing_postcode')
# postcode.send_keys('123456')
# time.sleep(3)
# driver.find_element_by_css_selector("[value='cheque']").click()
# driver.find_element_by_id('place_order').click()
# check_element_1= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# check_element_2= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>tr:nth-child(3)>td"), "Check Payments"))
# driver.quit()