from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

numero_dias = 7
numero_criancas = 2
atividades = "praia"

model_prompt = PromptTemplate(
    template="""
    Crie um roteiro de viagens, para um periodo de {numero_dias} dias,
    para uma familia com {numero_criancas} criancas, 
    que gostão de {atividades}
    """,

)

prompt = model_prompt.format(
    dias = numero_dias,
    numero_criancas = numero_criancas,
    atividades = atividades
)

print ("Prompt : \n", prompt)

modelo = ChatOpenAI(
    model='gpt-5-nano',
    temperature=0.5,
    api_key=api_key
)

reposta = modelo.invoke(prompt)
print(reposta.content)
