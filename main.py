from utils import *

# Ejecutar Menu
lista_jugadores_menu = menu()
jugador_activo = seleccionar_jugador_inicial(lista_jugadores_menu)

# //PREPARAR TABLEROS//
# Crear tablero J1
tablero_j1 = crear_tablero(10)
# Barcos a crear + vidas iniciales J1
lista_barcos_crear_j1 = [2,2,2,3,3,4]
vidas_j1 = len(lista_barcos_crear_j1)
print(f"Tienes {vidas_j1} activos")
lista_barcos_creados_j1 = []

# Crear barcos + pintar J1
lista_barcos_creados_j1 = colocar_barcos_sin_colision(lista_barcos_crear_j1,lista_barcos_creados_j1,tablero_j1)
print("Lista posiciones J1: ",lista_barcos_creados_j1)
pintar_barcos(lista_barcos_creados_j1,tablero_j1)
mostrar_tablero(tablero_j1)

# Crear tablero Computer
tablero_Computer = crear_tablero(10)
# Barcos a crear + vidas iniciales J1
lista_barcos_crear_Computer = [2,2,2,3,3,4]
vidas_Computer = len(lista_barcos_crear_Computer)
print(f"Computer tiene {vidas_Computer} esloras activas")
lista_barcos_creados_Computer = []

# Crear barcos + pintar Computer
lista_barcos_creados_Computer = colocar_barcos_sin_colision(lista_barcos_crear_Computer,lista_barcos_creados_Computer,tablero_Computer)
print("Lista posiciones Computer: ",lista_barcos_creados_Computer)
pintar_barcos(lista_barcos_creados_Computer,tablero_Computer)
mostrar_tablero(tablero_Computer)

# tiempo_y_limpiar_consola()

# Bucle del juego
while vidas_j1 > 0 or vidas_Computer > 0:
    if jugador_activo != "Computer":
        # jugador_activo = J1
        print("Turno del jugador 1")
        ataque = pedir_ataque()
        tablero,tocado = disparar(ataque,tablero_Computer)
        if tocado == True:
            # quita vida Computer
            vidas_Computer -= 1
            # sigues
            mostrar_tablero(tablero_Computer)
            # tiempo_y_limpiar_consola()
        else:
            # pasa turno a maquina
            jugador_activo = "Computer"
            #tiempo_y_limpiar_consola()
    else: 
        # jugador_activo = Computer
        print("Turno del Computer")
        ataque = ataque_aleatorio_maquina()
        tablero,tocado = disparar(ataque,tablero_j1)
        if tocado == True:
            # quita vida J1
            vidas_j1 -= 1
            # sigue la maquina
            mostrar_tablero(tablero_j1)
            #tiempo_y_limpiar_consola()
        else:
            # pasa turno al jugador
            jugador_activo = "Otro"
            #tiempo_y_limpiar_consola()

if jugador_activo != "Computer":
    print("FIN DEL JUEGO")
    print("Le has ganado al ordenador")
else:
    print("FIN DEL JUEGO")
    print("Te ha ganado el ordenador")