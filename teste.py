from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Carregando as variaveis de '.env'
load_dotenv()

# Chama a API do modelos da Open IA
model = ChatOpenAI(model="gpt-5-mini")

# Executa a chamada ao modelo
result = model.invoke("Este é um teste. Se você recebeu a requisição responda 'Teste OK'.")
print(result)