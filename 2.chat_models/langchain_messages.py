from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model = "gpt-5-mini",
    temperature = 0.1,
    #timeout 
    #max_tokens = 500,
    #max_retries,
    #api_key (ele puxa do env automaticamente)
)

messages = [
    SystemMessage(content = "Você é um especialista em astrofísica."),
    HumanMessage(content = "Qual a distância do sol até a terra?"),
    AIMessage(content = "O Sol está a 49.600.000 km de distância da terra."),
    HumanMessage(content = "E a distância da terra até marte?")
]

response = model.invoke(messages)

print(response)
print()
print()
print(response.content)