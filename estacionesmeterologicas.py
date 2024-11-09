from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#Instanciar y dimensionar

driver = webdriver.Chrome()
driver.set_window_position(0,0)
driver.set_window_size(1024,720)

#Solicitar url especifica
driver.get("https://courses.academti.com/chatbot/weather-stations/add")
time.sleep(10)

#Crearemos un diccionario: key , value
station_row = {
   'ID':'AGM00060580', 
   'Station Name':'OUARGLA', 
   'Elev-m':'150', 
   'Lat':'31.917', 
   'Lon':'5.413', 
   'Type':'Automatic', 
   'Temperature':'1', 
   'Atmospheric_Pressure':'0', 
   'Humidity':'0', 
   'Precipitation':'1', 
   'Radiation':'1' 
}


#Declarar variables

station_id = station_row['ID']
station_name = station_row['Station Name']
station_elevation = station_row['Elev-m']
station_lat = station_row['Lat']
station_lon = station_row['Lon']
station_type = station_row['Type']
station_atmospheric_pressure = station_row['Atmospheric_Pressure']
station_humidity = station_row['Atmospheric_Pressure']
station_precipitation = station_row['Precipitation']
station_radiation = station_row['Radiation']


#Nombres de los controles del formulario
station_id_element = driver.find_element(By.ID, 'stationId')
station_id_element.send_keys(station_id)
time.sleep(3)

station_name_element = driver.find_element(By.NAME, 'stationName')
station_name_element.send_keys(station_name)
time.sleep(3)

station_elevation_element = driver.find_element(By.CLASS_NAME, 'number')
station_elevation_element.send_keys(station_elevation)
time.sleep(3)

coordinate_elements = driver.find_elements(By.CLASS_NAME, 'coordinate')
coordinate_elements[0].send_keys(str(station_lat))
time.sleep(3)

coordinate_elements = driver.find_elements(By.CLASS_NAME, 'coordinate')
coordinate_elements[1].send_keys(str(station_lon))
time.sleep(3)



