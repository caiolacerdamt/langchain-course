from langchain_core.runnables import RunnableLambda

def sum(x: int) -> int:
    return x + 1

runnable = RunnableLambda(sum)

print(runnable.invoke(2))