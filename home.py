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
# driver.execute_script("window.scrollBy(0, 600);")
# driver.find_element_by_css_selector('.post-160').click()
# driver.find_element_by_class_name('reviews_tab').click()
# driver.find_element_by_class_name('star-5').click()
# review=driver.find_element_by_id('comment')
# review.send_keys("Nice book!")
# name=driver.find_element_by_id('author')
# name.send_keys('Иван')
# email=driver.find_element_by_id('email')
# email.send_keys('ivanov@yandex.ru')
# driver.find_element_by_id('submit').click()
# driver.quit()