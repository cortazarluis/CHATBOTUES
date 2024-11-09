from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from openai import OpenAI
import os

#Crear cliente 
client =OpenAI(
    api_key = os.getenv('OPENAI_API_KEY')
)

#Generar funcion
def call_endpoint(messages):
    chatgpt_messages_list = [
        {"role":"system","content":'''
         Eres un profesor de la Universidad Estatal de Sonora, solo puedes contestar con relacion al contenido:
          mi correo electronico es: julian.flores@ues.mx, mi telefono es: 6621048354
          Las materias con las que trabajo en el semestre actual son:
          1.- Materia Programacion Avanzada, url://www.ues.x, dia: lunes a Viernes
          2.- Materia Programacion para Dispositivos Moviles, url://www.ues.x, dia: lunes a Viernes
          3.- Inteligencia Artificial, url://www.ues.x, dia: lunes a Viernes'''}
    ]
    
    chatgpt_response = chatgpt_messages_list + messages
    
    chatgpt_response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        temperature=0.2,
        messages = messages
    )
    
    assistant_message = chatgpt_response.choices[0].message.content
    
    return assistant_message

#Colocar opciones
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\SERVIDOR\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

#Instanciar y dimensionar
driver = webdriver.Chrome(options=options)
driver.set_window_position(0,0)
driver.set_window_size(1024,720)

#implementar tiempo de espera
driver.implicitly_wait(3600)

#Solicitar url especifica
driver.get("https://web.whatsapp.com")

#Cambiamos
while (True):
    
    #Expresiones xpath
    #//*[@id="pane-side"]/descendant::span[contains(@aria-label,'no leidos')]
    #//*[@id="main"]/descendant::div[@role='row']
    #//div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span
    #//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]

    #Recuperamos nuevos mensajes
    new_message = driver.find_element(By.XPATH, '//*[@id="pane-side"]/descendant::span[contains(@aria-label,\'no leído\')]')
    new_message.click()
    
    #Obtener los mensajes del usuario
    last_messages = driver.find_elements(By.XPATH, '//*[@id="main"]/descendant::div[@role=\'row\']')
    last_message = last_messages[-1]
    
    #Mostrar mensaje seleccionado
    last_message_text = last_message.find_element(By.XPATH, '//div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span')
    print(f'user message:{last_message.text}')
    
    #Establecemos la lista
    
    message_list = []
    message_list.append({'role':'user','content': last_message_text})
   
    #Notificar al usuario
    print('sending message to language service')
    #api_message = "Mesa de respuesta desde la API"
    
    api_message = call_endpoint(message_list)
    message_element = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]')
    message_element.send_keys(f'{api_message}{Keys.ENTER}')
    message_element.send_keys(Keys.ESCAPE)

