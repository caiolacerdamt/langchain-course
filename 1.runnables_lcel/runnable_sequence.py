from langchain_core.runnables import RunnableLambda, RunnableSequence

def sum(x: int) -> int:
    return x + 1

def mult(x: int) -> int:
    return x * 3

runnable_1 = RunnableLambda(sum)
runnable_2 = RunnableLambda(mult)

sequence = runnable_1 | runnable_2

# Equivalente
# sequence = RunnableSequence(
#     first = runnable_1,
#     last = runnable_2
# )

print(sequence.invoke(2))