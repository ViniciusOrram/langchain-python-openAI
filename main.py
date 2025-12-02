from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

numero_dias = 7
numero_criancas = 2
atividades = "musica"

prompt = f"Crie um roteiro de viagem de {numero_dias} dias, para uma familia com {numero_criancas} criancas, que gosta de {atividades}"

client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {
            "role": "system", 
            "content": "Você é um assistente de viagem que cria roteiros de viagem para famílias."
        },
        {
            "role": "user", 
            "content": prompt
        }
    ]
)
response_text = response.choices[0].message.content
print(response_text)