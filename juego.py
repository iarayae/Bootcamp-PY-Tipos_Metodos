from personaje import Personaje
import random

# Inicio del juego
print("¡Bienvenido a Gran Fantasía!")
nombre_jugador = input("Por favor indique nombre de su personaje: ")

# Crear personaje del jugador con nivel 1 y experiencia 0
jugador = Personaje(nombre_jugador)
jugador.estado  # Mostrar estado inicial

# Crear oponente: el Orco
orco = Personaje("Orco")
orco.estado  # Mostrar estado del orco

# Calcular probabilidad inicial de victoria
prob = jugador.probabilidad_ganar(orco)

# Mostrar mensaje y obtener acción del jugador
opcion = Personaje.mostrar_dialogo(prob)

# Ciclo principal: mientras el jugador quiera atacar
while opcion == "1":
    resultado = random.uniform(0, 1)  # Genera número aleatorio entre 0 y 1

    if resultado <= prob:
        # Jugador gana
        print("\n¡Le has ganado al orco, felicidades!")
        print("¡Recibirás 50 puntos de experiencia!")
        jugador.estado = 50
        orco.estado = -30
    else:
        # Jugador pierde
        print("\n¡Oh no! ¡El orco te ha ganado!")
        print("¡Has perdido 30 puntos de experiencia!")
        jugador.estado = -30
        orco.estado = 50

    # Mostrar estados actualizados de ambos personajes
    jugador.estado
    orco.estado

    # Calcular nueva probabilidad de victoria
    prob = jugador.probabilidad_ganar(orco)

    # Volver a mostrar diálogo y consultar acción
    opcion = Personaje.mostrar_dialogo(prob)

# Si el jugador decide huir
if opcion == "2":
    print("\n¡Has huido! El orco ha quedado atrás.")