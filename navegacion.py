from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.set_window_position(0,0)
driver.set_window_size(1024,720)

#Navegacion hacia whatsapp
driver.get("https://web.whatsapp.com")
time.sleep(15)

#Navegacion hacia url
driver.get("https://www.google.com")
print(driver.title)
time.sleep(15)

#Metodo back
driver.back()
print(driver.current_url)
time.sleep(15)

#Metodo forward
driver.forward()
print(driver.current_url)
time.sleep(15)

#Metodo refresh
driver.refresh()
print(driver.current_url)
time.sleep(15)
