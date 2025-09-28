from langchain_core.runnables import RunnableLambda, RunnableParallel

def sum(x: int) -> int:
    return x + 1

def mult_2(x: int) -> int:
    return x * 2

def mult_3(x: int) -> int:
    return x * 3

runnable_sum = RunnableLambda(sum)
runnable_mult2 = RunnableLambda(mult_2)
runnable_mult3 = RunnableLambda(mult_3)

#Equivalente
# parallel = runnable_sum | {
#     "mult_2": runnable_mult2,
#     "mult_3": runnable_mult3
# }

parallel = runnable_sum | RunnableParallel(
    mult_2 = runnable_mult2,
    mult_3 = runnable_mult3
)

# Equivalente
# parallel = runnable_sum | RunnableParallel({
#     "mult_2": runnable_mult2,
#     "mult_3": runnable_mult3
# })

print(parallel.invoke(1))