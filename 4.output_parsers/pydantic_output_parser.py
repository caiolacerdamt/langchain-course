from dotenv import load_dotenv
load_dotenv()

from langchain_core.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_openai.chat_models import ChatOpenAI
from pydantic import BaseModel, Field

model = ChatOpenAI(model="gpt-5-mini")

class Rota(BaseModel):
    escolha: int = Field(description="Rota escolhida")
    pensamento: str = Field(description="Campo para o pensamento que levou a decisão da rota escolhida")

parser = PydanticOutputParser(pydantic_object=Rota)

prompt_template = ChatPromptTemplate([("system",
                                       "Se a pergunta do usuário for relacionado ao setor financeiro, \
                                       a escolha deve ser 1, caso contrário a escolha pode ser qualquer numero \
                                       diferente de 1. \n{format_instructions}\n Pergunta Usuário: {pergunta_user}")],
                                     partial_variables={"format_instructions": parser.get_format_instructions()})

chain = prompt_template | model | parser

output = chain.invoke({"pergunta_user": "Me diga quanto está o dolar"})

print(output)
print("----"*40)
print(output.escolha)
print("----"*40)
print(output.pensamento)