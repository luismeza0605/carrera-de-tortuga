from turtle import * #Aqui se importa el dibujo de las tortugas
from random import randint # aqui se importa la libreria rango para poderlo usar los numeros a la azar
speed(0)  # Su funcion es darle la velocidad de las tortugas
penup()    #levanta el lapiz de la tortuga 
goto(-140,140) #posiciona la tortuga en la esquena superior izquierda

for paso in range(15): 
    write(paso, align='center')  # Escribe el número de paso en el centro
    right(90)  # Gira la tortuga hacia la derecha
    forward(10)  # Avanza 10 unidades

    for dash in range (10):
        pendown()
        forward(7)
        penup()
        forward(8)

    penup()  # Levanta el lápiz
    backward(160)  # Retrocede para regresar al inicio
    left(90)  # Gira la tortuga hacia la izquierda
    forward(20)  # Avanza para la próxima línea    


ana = Turtle()
ana.color('red')
ana.shape('turtle')

ana.penup()
ana.goto(-160,100)
ana.pendown()

juan= Turtle()
juan.color('blue')
juan.shape('turtle')

juan.penup()
juan.goto(-160,70)
juan.pendown()

luis = Turtle()
luis.color('green')
luis.shape('turtle')

luis.penup()
luis.goto(-160,50)
luis.pendown()

eddy = Turtle()
eddy.color('yellow')
eddy.shape('turtle')

eddy.penup()
eddy.goto(-160,30)
eddy.pendown()

nayeli = Turtle()
nayeli.color('pink')
nayeli.shape('turtle')

nayeli.penup()
nayeli.goto(-160,15)
nayeli.pendown()

def girar_360(tortuga):
    for _ in range(36):
        tortuga.right(10)

for girar2 in range(100):
    ana.forward(randint(1,5))
    juan.forward(randint(1,5))
    luis.forward(randint(1,5))
    eddy.forward(randint(1,5))
    nayeli.forward(randint(1,5))


girar_360(ana)
girar_360(juan)
girar_360(luis)
girar_360(eddy)
girar_360(nayeli)

done()  
