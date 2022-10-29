import turtle


def drawTriangle(tortuga, x, y, lado):
    tortuga.penup()
    tortuga.setposition(x, y)
    tortuga.pendown()
    
    for _ in range(0, 3):
        tortuga.forward(lado)
        tortuga.left(120)
        
def alturaEquilatero(lado):
  return 3 ** 0.5 * lado / 2

def perimetroEquilatero(lado):
  return 3 * lado

def superficieEquilatero(lado):
  return lado * alturaEquilatero(lado) / 2

def triangulo(tortuga, lado, x=0, y=0):
  drawTriangle(tortuga, x, y, lado)
  print("Perímetro:  ", perimetroEquilatero(lado), " pixels")
  print("Superficie: ", superficieEquilatero(lado), " pixels^2")
  

if __name__ == '__main__':
  triggy = turtle.Turtle()
  triggy.speed(99)

  triangulo(triggy, 150)