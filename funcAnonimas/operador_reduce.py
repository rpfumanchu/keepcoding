from sumas import sumatorio
from functools import reduce

#print(sumatorio(15, lambda x: 2 * x + 1))

print(
    reduce(lambda a, b: a + b, range(100 + 1)),
    #esto es igual que decir....
    sumatorio(100)
)

# con reduce nos da un valor distinto porque en el acumulado toma 0 pero no lo procesa, por eso necesitamos meterle un inicializador
print(
    reduce(lambda a, b: a + 2 * b + 1, range(15 + 1)), 
    sumatorio(15, lambda x: 2 * x + 1)
)    

print(
    reduce(lambda a, b: a + 2 * b + 1, range(15 + 1), 0), 
    sumatorio(15, lambda x: 2 * x + 1)
)    