from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough, RunnableSequence

part_1 = RunnablePassthrough()

def conta_caracteres(x: dict) -> int:
    return len(x["input"])

convert_function = RunnableLambda(conta_caracteres)

part_2 = RunnablePassthrough.assign(num_caract = convert_function)

def transform(x: dict) -> str:
    result = x["input"] + " Conseguiu!"
    return result

part_3_transform_entrada = RunnableLambda(transform)
part_3_passa_frente = RunnablePassthrough()

part_3 = RunnableParallel({
    "transformar_entrada": part_3_transform_entrada,
    "passar_para_frente": part_3_passa_frente
})

part_4 = RunnablePassthrough()

chain = part_1 | part_2 | part_3 | part_4


resposta = chain.invoke({"input": "Parabéns você"})

print(resposta)