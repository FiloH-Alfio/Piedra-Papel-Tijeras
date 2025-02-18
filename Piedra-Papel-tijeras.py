nombre1 = input ("Como se llamará el Jugador 1?: ")
nombre2 = input ("Como se llamará el Jugador 2?: ")



Jugador1 = input("Bienvenido " + nombre1 + "! qué elegis? Piedra, Papel o Tijeras?: ")
Jugador2 = input("Bienvenido " + nombre2 + "! qué elegis? Piedra, Papel o Tijeras?: ")


condicion1 = Jugador1 == "piedra" and Jugador2 == "tijeras"
condicion2 = Jugador1 == "papel" and Jugador2 == "piedra"
condicion3 = Jugador1 == "tijeras" and Jugador2 == "papel"

if Jugador1 == Jugador2:
    print("Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print("Has ganado", nombre1)
else:
    print("Has ganado", nombre2)

