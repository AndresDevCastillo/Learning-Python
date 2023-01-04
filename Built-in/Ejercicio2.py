from functools import reduce

Numeros = []
for i in range(1, 100):
    Numeros.append(i)


NumImpar = filter(lambda x: x % 2, Numeros)
SumAll = reduce(lambda a,b: a+b , NumImpar)
print(Numeros)
print(list(NumImpar))
print(SumAll)




