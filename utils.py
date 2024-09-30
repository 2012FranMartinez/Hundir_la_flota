import numpy as np
import random
import os
import time


# [TABLERO]
def crear_tablero(dimension):
    """Inicializa el tablero vacío."""
    tablero = np.full((dimension, dimension), "_")
    return tablero

def mostrar_tablero(tablero):
    """Muestra el tablero en pantalla."""
    print("El tablero:")
    print(tablero)

def pintar_barcos(lista_barcos, tablero):
    """Coloca los barcos en el tablero."""
    for tupla in lista_barcos:
        for casilla in tupla:
            tablero[casilla] = "B"
    return tablero

# [BARCOS]
def crear_barco_en_limites(eslora, tablero):
    """Crea un barco dentro de los límites del tablero."""
    dimension = len(tablero)
    barco_posiciones = []
    dentro_limites_tabl = False

    while not dentro_limites_tabl:
        casilla_0 = (random.randint(0, dimension - 1), random.randint(0, dimension - 1))

        if casilla_0[0] < (dimension / 2):
            orientacion = random.choice(["Vertical", "Horizontal"])
            barco_posiciones = [casilla_0]
            casilla = casilla_0

            while len(barco_posiciones) < eslora:
                if orientacion == "Vertical":
                    casilla = (casilla[0], casilla[1] + 1)
                elif orientacion == "Horizontal":
                    casilla = (casilla[0] + 1, casilla[1])
                
                if casilla[0] < dimension and casilla[1] < dimension:
                    barco_posiciones.append(casilla)
                else:
                    break

            if len(barco_posiciones) == eslora:
                dentro_limites_tabl = True
                return barco_posiciones

def almacenar_barcos_creados(lista_contuplas, lista_devolver):
    """Almacena las tuplas de barcos creados en una lista."""
    for x in lista_contuplas:
        lista_devolver.append(x)
    return lista_devolver

def comprobar_colision_barco_creado(barco, lista):
    """Comprueba si el barco colisiona con otro ya colocado."""
    for tupla_comparar in barco:
        if len(lista) == 0:
            colision_barcos = True
        else:
            for x in range(len(lista)):
                for i in lista[x]:
                    if i == tupla_comparar:
                        colision_barcos = False
                        return colision_barcos
                    else:
                        colision_barcos = True
    return colision_barcos

def colocar_barcos_sin_colision(lista_barcos_crear, lista_barcos_creados, tablero):
    """Coloca los barcos en el tablero sin colisionar entre sí."""
    for i in lista_barcos_crear:
        colocado = False
        while not colocado:
            try:
                barco = crear_barco_en_limites(i, tablero)
                colocado = comprobar_colision_barco_creado(barco, lista_barcos_creados)
                if colocado:
                    lista_barcos_creados.append(barco)
            except Exception as e:
                print(f"Error creando o colocando el barco: {e}")
    return lista_barcos_creados

# [JUGADORES Y TURNOS]
def menu():
    """Muestra el menú principal y gestiona la elección de jugadores."""
    lista_jugadores = []

    print("*" * 20)
    print("\tMENU")
    print("¿Cómo quieres jugar?")
    print("[A] Contra el ordenador")
    print("[B] Multijugador")
    print("*" * 20)
    respuesta_menu = input("Escribe A o B: ").upper()

    if respuesta_menu == "A":
        print("Contra el ordenador, vale")
        nombre_user = solicitar_nombre()
        lista_jugadores.append(nombre_user)
        lista_jugadores.append("Computer")
        print(lista_jugadores)
        return lista_jugadores      
    elif respuesta_menu == "B":
        pass  # Para implementar en el futuro

def seleccionar_jugador_inicial(lista_jugadores):
    """Selecciona de manera aleatoria el jugador inicial."""
    eleccion = random.choice(lista_jugadores)
    return eleccion

def cambio_jugador(jugador_activo, lista_jugadores):
    """Cambia el turno entre los jugadores."""
    if jugador_activo == lista_jugadores[0]:
        return lista_jugadores[1]
    else:
        return lista_jugadores[0]

def solicitar_nombre():
    """Solicita el nombre del usuario."""
    nombre_user = input("Indica el nombre del usuario: ")
    print(f"Ok {nombre_user}, comencemos.")
    return nombre_user

def quitar_vidas(vidas):
    """Reduce en 1 las vidas restantes del jugador."""
    return vidas - 1

def tiempo_y_limpiar_consola():

    os.system('cls')
    time.sleep(1)


# [COMBATE]
def disparar(casilla, tablero):
    """Realiza un disparo a una casilla del tablero."""
    tocado = False
    if tablero[casilla] == "B":
        print("Tocado")
        tablero[casilla] = "X"
        tocado = True
    else:
        print("Agua")
        tablero[casilla] = "A"
        tocado = False
    return tablero, tocado

def pedir_ataque():
    """Solicita las coordenadas de ataque al jugador."""
    while True:
        ataque = input("Introduce tu ataque (formato: número.número): ")
        if '.' in ataque:
            coordenadas = ataque.split('.')
            if len(coordenadas) == 2 and coordenadas[0].isdigit() and coordenadas[1].isdigit():
                fila = int(coordenadas[0])
                columna = int(coordenadas[1])
                return (fila, columna)
            else:
                print("Formato incorrecto. Asegúrate de introducir dos números separados por un punto.")
        else:
            print("Formato incorrecto. Debe contener un punto.")

def ataque_aleatorio_maquina():
    fila = random.randint(0, 9)
    columna = random.randint(0, 9)
    return (fila, columna)

























