from langchain_core.runnables import RunnablePassthrough, RunnableAssign

dict = {"num": 3}

chain = RunnablePassthrough() | RunnablePassthrough.assign(mult_3 = lambda x: x["num"] * 3)

print(chain.invoke(dict))