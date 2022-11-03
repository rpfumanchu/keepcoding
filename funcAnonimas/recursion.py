from sumas import sumatorio, sumaTodosAlcuadrado

#podemos ponerle un 1 o un 0 porque el factorial de 0 también es 1
def sumatorioR(n):
    if n <= 0:
        return 0
    else:
        return n + sumatorioR(n - 1)

#tambien podemos hacerlo con una funcion
def sumatorioR_funcion(n, sumaTososAlcuadrado):
    if n <= 0:
        return sumaTodosAlcuadrado(0)
    else:
        return n + sumatorioR_funcion(n - 1, sumaTodosAlcuadrado)

def sumatorioR_funcion2(n, sumatorio):
    if n <= 0:
        return sumatorio
    else:
        return n + sumatorioR_funcion(n - 1, sumatorio)

print(sumatorioR(100), sumatorio(100))
print(sumatorioR_funcion(100,0))
print(sumatorioR_funcion2(100,0))

#python tiene capada la recursion a 1000 porque consume muchos recursos, si lo hacemos peta

# print(sumatorio(1000))
# print(sumatorioR(1000))