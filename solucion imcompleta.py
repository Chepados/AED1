from pprint import pprint
from copy import deepcopy

FILA = 0
COLUMNA = 1
fail = None

def visualizar_estado(maze):
    for i in range(len(maze)):
        for j in range(len(maze)):
            print(maze[i][j], end="")
        print()

def load_maze():

    maze_matrix = []

    with open("maze.txt", "r") as maze:
        while (row := maze.readline()) != "":
            row_matrix = []
            for char in row:
                match char:
                    case "#":
                        row_matrix.append("#")
                    case " ":
                        row_matrix.append(" ")
                    case "I":
                        row_matrix.append(" ")
                        start_pos = (len(maze_matrix), row.index("I"))
                    case "F":
                        row_matrix.append(" ")
                        end_pos = (len(maze_matrix), row.index("F"))
            maze_matrix.append(row_matrix)

    return maze_matrix, start_pos, end_pos

maze_matrix, start_pos, end_pos = load_maze()

copia_maze = deepcopy(maze_matrix)

stack = [start_pos]

while len(stack) != 0 and stack[-1] != end_pos:

    y_current = stack[-1][0]
    x_current = stack[-1][1]


    #Hay que tener en cuenta que te puedes salir de la matriz con algunos laberintos Indexerror

    if maze_matrix[y_current - 1][x_current] == " ":
        stack.append((y_current - 1,x_current))
    elif maze_matrix[y_current][x_current + 1] == " ":
        stack.append((y_current,x_current + 1))
    elif maze_matrix[y_current + 1][x_current] == " ":
        stack.append((y_current + 1,x_current))
    elif maze_matrix[y_current][x_current - 1] == " ":
        stack.append((y_current,x_current - 1))
    else:
        if maze_matrix != fail:
            visualizar_estado(maze_matrix)
            fail = deepcopy(maze_matrix)
        print("Me he chocado ;(")
        stack.pop()

    maze_matrix[y_current][x_current] = "V"

#VISUALIZAR SOLUCION

for i in range(len(copia_maze)):
    for j in range(len(copia_maze)):
        if (i, j) in stack:
            copia_maze[i][j] = "*"

print(stack)
visualizar_estado(copia_maze)
