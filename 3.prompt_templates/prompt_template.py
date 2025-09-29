from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Gere para mim um poema sobre: {assunto}. Escreva em {lingua}"
)

retorno = prompt_template.invoke({
    "assunto": "futebol",
    "lingua": "inglês"
})

print(retorno)