from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

prompt_cidade = PromptTemplate(
    template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    """
    input_variables=["interesse"]
)
modelo = ChatOpenAI(
    model='gpt-5-nano',
    temperature=0.5,
    api_key=api_key
)

cadeia = prompt_cidade | modelo | StrOutputParser()

reposta = cadeia.invoke(
    {
        "interesse" : "praias"
    }
)
print(reposta)
