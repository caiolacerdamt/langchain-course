from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_core.messages import HumanMessage

prompt_template = ChatPromptTemplate([
    ("system", "Você é um assistente de IA com habilidade de escritor de poeisa."),
    MessagesPlaceholder("msgs_user")
])

retorno = prompt_template.invoke(
    {"msgs_user": [HumanMessage(content="Gere um poema sobre: navegação. Escreva em pt-br")]}
)

print(retorno)