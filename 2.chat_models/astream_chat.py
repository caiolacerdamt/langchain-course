from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio

load_dotenv()

async def conversa():
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
        print()
        entrada = input("Entrada Usuário (digite q para sair):")
        print()
        if entrada.lower() == 'q':
            break

        conversa.append(HumanMessage(content = entrada))

        all_chunk = []
        async for chunk in llm.astream(conversa):
            all_chunk.append(chunk.content)
            print(chunk.content, end="", flush=True)

        resposta_completa = "".join(all_chunk)
        conversa.append(AIMessage(content=resposta_completa))

    print("Histórico da Conversa")
    print(conversa)

asyncio.run(conversa())