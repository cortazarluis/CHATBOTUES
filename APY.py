from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

#Definicion del cliente
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

#Respuesta
response=client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    #max_tokens=10, maximo de tokens
    temperature=0.2, #temperatura de 0.1 a 0.9
    messages=[
        {"role":"system","content":'''
         Eres un profesor de la Universidad Estatal de Sonora 
          1.- Materia Programacion Avanzada, url://www.ues.x, dia: lunes a Viernes
          2.- Materia Programacion para Dispositivos Moviles, url://www.ues.x, dia: lunes a Viernes
          3.- Inteligencia Artificial, url://www.ues.x, dia: lunes a Viernes'''},
        {"role":"user","content":"¿Hola, buenas tardes?"}
        {"role":"user","content":"¿Que tipo de cursos impartes?"}
    ]
)

#Enviamos a impresion
print(response)