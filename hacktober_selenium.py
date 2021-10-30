from selenium import webdriver                                          #селентиум
import time                                                             #временной отрезок
from selenium.webdriver.common.by import By                             #импортируем by

driver = webdriver.Firefox()                                            #говорим что у нас Firefox, драйвер который будет взаимодейтвовать с ним напрямую
driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=ru&flowName=GlifWebSignIn&flowEntry=ServiceLogin')                                        #вызываем youtube
time.sleep(1.5)                                                         #ставим задержку на 1.5 секунды, чтобы успела прогрузиться страница
# try:                                                                  #при получении ссылки на верификацию,
# активируем ее
#
# except: element = driver.find_element(By.XPATH,
# """"/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/dia[2]/div[2]/div[5]/div[
# 2]/ytd-button-renderer[2]""") element.click()

search_bar = driver.find_element(By.XPATH, """//input[@id="search"]""")     #находим поле для ввода текста(поисковой запрос)
search = 'pochta'                                                            #вводим запрос в консоль
search_bar.send_keys(search)                                                #вводим запрос
searchbutton = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')       #находим кнопку
searchbutton.click()                                                                #нажимаем кнопку
                                                   #нажимаем на него


"""
https://selenium-python.readthedocs.io/locating-elements.html
"""
