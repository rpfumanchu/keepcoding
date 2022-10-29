def debug(f): # f es la función de entrada que será decorada por debug
  def out_f(*args): # out_f será la función de salida que devolverá debug.
                    # tendrá los mismos argumentos que f (con el truco de *args nos evitamos firma de función)
    ''' Imprimir los argumentos de f '''
    i = 1
    for arg in args:
      print("argumento {}: {}".format(i, arg))
      i += 1
    ''' Devolver la ejecución de la función de entrada con sus parámetros.
        Así no se modifica la acción de f
    '''
    return f(*args)
  
  return out_f #devuelve la función decorada con la impresión

@debug
def add(a, b):
  return a+b

@debug
def square(a):
  return a*a

@debug
def triangle(b,h):
  return b*h/2
print(add(1,2))
print(square(3))
print(triangle(4,5))