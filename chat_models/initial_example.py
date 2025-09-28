from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model = "gpt-5-mini",
    temperature = 0.1,
    #timeout 
    #max_tokens = 100,
    #max_retries,
    #api_key (ele puxa do env automaticamente)
)

response = model.invoke("O que você é capaz de fazer? Em 50 palavras")

print(response)
print(response.content)