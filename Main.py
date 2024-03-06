from Maze import Maze
import os

lista_laberintos = os.listdir("laberintos")

finalizado = False
while not finalizado:

    entrada = input("\n(A)Buscar un laberito concreto.\n(B)Ver opciones y seleccionar.\n(C)Salir.\n\n")

    if entrada.upper() == "A":
        laberinto = input("Escribe el nombre del laberinto que deseas cargar: ")
        if laberinto in lista_laberintos:
            maze = Maze(laberinto)
    elif entrada.upper() == "B":
        for i, laberinto in enumerate(lista_laberintos):
            print(f"({i}) {laberinto}")

        indice_laberinto = int(input("\nEscribe tu seleccion: "))

        if indice_laberinto in range(len(lista_laberintos)):
            maze = Maze(lista_laberintos[indice_laberinto])
    else:
        finaliado = True


    print(f"Solucion encontrada al laberinto: {maze.find_path()}\n")

    print("Visualizacion de la solucion:\n")

    maze.show_path()