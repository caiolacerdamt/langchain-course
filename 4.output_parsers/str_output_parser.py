from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash"
)

prompt_template = ChatPromptTemplate(
    [("user", "Escreva um poema em {lingua} sobre o tema: {assunto}")]
)

output_parser = StrOutputParser()

chain = prompt_template | model | output_parser

response = chain.invoke({"lingua": "inglês", "assunto": "frutas"})

print(type(response))
print("---"*50)
print(response) # --> Não precisa mais do .content
