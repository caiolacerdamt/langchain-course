from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.1,
    max_tokens=None,
    timeout=None,
)

conversa = [
    SystemMessage(content = "Você é um asssistente útil que responde ao usuário de forma seca, curta, descontraída, engraçada e com deboche.")
]

while True:
    entrada = input("Entrada Usuário (digite q para sair):")
    if entrada.lower() == 'q':
        break

    conversa.append(HumanMessage(content = entrada))

    resultado = llm.invoke(conversa)
    resposta = resultado.content
    conversa.append(AIMessage(content = resposta))

    print(f"Resposta da IA: {resposta}")

print("Histórico da Conversa")
print(conversa)