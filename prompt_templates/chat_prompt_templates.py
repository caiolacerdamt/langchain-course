from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate(
    [
        "Gere para mim um poeme sobre: {assunto}. Escreva em {lingua}"
    ]
)

retorno = prompt_template.invoke(
    {
        "assunto": "futebol",
        "lingua": "inglês"
    }
)

print(retorno)
