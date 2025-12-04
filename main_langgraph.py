from typing import Literal, TypedDict
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

from main_chat import api_key

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

modelo = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0.5,
    api_key = api_key
)

prompt_consultor_praia = ChatPromptTemplate.from_template(
    [
        ("system", "Apresente-se como Sra Praia. Você é uma especialista em viagens com destinos para a praia.")
        ("human", "{query}")
    ]
)

prompt_consultor_montanha = ChatPromptTemplate.from_template(
    [
        ("system", "Apresente-se como Sra Montanha. Você é uma especialista em viagens com destinos para montanhas e atividades radicais.")
        ("human", "{query}")
    ]
)

cadeia_praia = prompt_consultor_praia | modelo | StrOutputParser()
cadeia_montanha = prompt_consultor_montanha | modelo | StrOutputParser()

class Rota(TypedDict):
    destino: Literal["praia", "montanha"]



prompt_roteador = ChatPromptTemplate.from_messages(
    [
        ("system", "Responda apenas com 'praia' ou 'montanha'"),
        ("human", "{query}")
    ]
)

roteador = prompt_roteador | modelo.with_structured_output(Rota)

def response(pergunta : str):
    rota = roteador.invoke({"query" : pergunta})["destino"]

    if rota == "praia":
        return cadeia_praia.invoke({"query" : pergunta})
    return cadeia_montanha.invoke({"query" : pergunta})

print(response("Quero passear por praias belas no Brasil."))