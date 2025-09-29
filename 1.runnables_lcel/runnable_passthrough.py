from langchain_core.runnables import RunnablePassthrough

chain = RunnablePassthrough() | RunnablePassthrough() | RunnablePassthrough()

print(chain.invoke("Olá"))