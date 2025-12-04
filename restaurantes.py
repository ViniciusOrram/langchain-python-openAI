from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from pydantic import Field, BaseModel
from dotenv import load_dotenv
from langchain.globals import set_debug

from main import modelo

class Restaurantes(BaseModel):
    cidade:str = Field("A cidade recomenda para visitar")
    motivo:str = Field("Restaurantes recomendados na cidade")

parseador_restaurantes = JsonOutputParser(pydantic_object=Restaurantes)

prompt_restaurantes = PromptTemplate(
    template="""
    Sugira restaurantes populares entre locais em {cidades}.
    {formato_de_saida}
    """,
    partial_variables={"formato_de_saida": parseador_restaurantes.get_format_instructions()}
)

prompt_cultural = PromptTemplate(
    template="Sugira atividades e locais culturais em {cidades}"
)

cadeia_1 = prompt_restaurantes | modelo | parseador_restaurantes
