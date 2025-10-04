from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda

model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)

def separador_de_tweet(entrada: str) -> list:
    """
    Função que recebe uma strin e retorna uma lista com os elementos
    separados por quebras de linha.

    Args:
        entrada (str): A string entrada, onde os valores estão separados por
        quebras de linha.

    Returns:
        list: Uma lista contendo cada elemento da string como um item separado
    """

    elementos = entrada.split("\n")

    elementos_limpos = [elemento.strip() for elemento in elementos if elemento.strip()]

    return elementos_limpos

def relatorio_de_analise_de_caracteres(entrada: list) -> dict:
    """
    Função que gera um relatório com os tweets e a contagem de caracteres
    de cada tweet.

    Args:
        entrada(list): Lista de strings representando os tweets.

    Returns:
        dict: um dicionário com duas chaves:
            - 'tweets': contendo a lista original
            - 'num_caract': contendo uma lista com o número de caracteres de cada tweet.
    """

    contagem_caracteres = [len(tweet) for tweet in entrada]

    relatorio = {
        'tweets': entrada,
        'num_caract': contagem_caracteres
    }

    return relatorio

system_prompt = """"
        Você é um assistente especialista em criar conteúdo para o twitter
        e tem como objetivo criar os melhores tweets virais sobre o tema
        que o usuário te passar. Seja criativo e atenda ao padrão de 280 
        caracteres do twitter.
        Orientação:
        - Crie apenas o número de tweets informado.
        - Separe cada um deles por uma quebra de linha.
"""

prompt_template = ChatPromptTemplate(
    [
        ("system", system_prompt),
        ("human", "Crie um total de {posts} tweets sobre o tema {theme}")
    ]
)

chain = prompt_template | model | StrOutputParser() | RunnableLambda(separador_de_tweet) | RunnableLambda(relatorio_de_analise_de_caracteres)

result = chain.invoke({"posts": 3, "theme": "tecnologia"})

print(result)
print("--"*40)

for i, (tweet, num_caract) in enumerate(zip(result['tweets'], result['num_caract']), start=1):
    print(f"Tweet {i}: {tweet}")
    print(f"Total de caracteres: {num_caract}")
    if num_caract <= 280:
        print("Validação: OK")
    else:
        print("Validação: Falha")
    print("--"*40)