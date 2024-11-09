from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

#Definicion del cliente
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

#Mensajes

messages=[
        {"role":"system","content":'''
            Eres un profesor de la Universidad Estatal de Sonora 
            1.- Materia Programacion Avanzada, url://www.ues.x, dia: lunes a Viernes
            2.- Materia Programacion para Dispositivos Moviles, url://www.ues.x, dia: lunes a Viernes
            3.- Inteligencia Artificial, url://www.ues.x, dia: lunes a Viernes'''}
        ]

#Interactividad
user_message = ''

#Declarar bucle

while(user_message != 'exit'):
    
    #Cargar mensaje del usuario en una variable
    print("Redactar el mensaje del usuario")
    user_message = input()
    
    #Manejo del historial y de los mensajes
    if len(messages) >=1 and len(messages) <= 4:
        messages.append({'role':'user','content': user_message})
    else:    
        #Colocar bucle for
        for i in range(3, len(messages), 2):
            messages[i-2] = messages[i]
            messages[i-1] = messages[i+1]
        
        messages[len(messages)-2] = {'role':'user','conten':user_message}
        messages.pop
        
    #Establecemos la respuesta
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        temperature=0.2,
        messages=messages
    )
    
    assistant_message = response.choices[0].message.content
    print(f"La API responde de la siguiente manera --> {assistant_message}")
    
    #Despues de la llamada api
    print("Despues de la llamada a la API, tenemos la siguiente respuesta -->")
    print(messages) 