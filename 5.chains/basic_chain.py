from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)

system_prompt = """"
        Você é um assistente especialista em criar conteúdo para o twitter
        e tem como objetivo criar os melhores tweets virais sobre o tema
        que o usuário te passar. Seja criativo e atenda ao padrão de 280 
        caracteres do twitter.
"""

prompt_template = ChatPromptTemplate(
    [
        ("system", system_prompt),
        ("human", "Crie um total de {posts} tweets sobre o tema {theme}")
    ]
)

chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"posts": 2, "theme": "tecnologia"})

print(result)