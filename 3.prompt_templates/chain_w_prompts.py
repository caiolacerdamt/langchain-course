from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt_template = ChatPromptTemplate([
    ("user", "Escreva um poema em {lingua} sobre o tema: {assunto}")
])

chain = prompt_template | model

resposta = chain.invoke({"lingua": "pt-br", "assunto": "futebol"})

print(resposta.content)
