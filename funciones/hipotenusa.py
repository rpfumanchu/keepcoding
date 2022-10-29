import math
# distinta opciones para optimizar codigo y reusar funciones




def hipotenusa(c1, c2):
     h = math.sqrt(c1*c2 + c2*c2)
     return h

def hcartabon(l):
     return hipotenusa(l, l)



# al ponerle un -1 a c2 conseguimos hacer que sea un parametro por defecto
# def hipotenusa(c1, c2 = -1):
#     if c2 == -1:
#         h = math.sqrt(c1*c1 + c2*c2)
#     else:
#         h = math.sqrt(c1*c1 + c2*c2)
#     return h


cateto1 = 3
cateto2 = 4
_hcartabon = hcartabon(cateto1)
_hipotenusa = hipotenusa(cateto1, cateto2)
