from copy import deepcopy
from LinkedStack import Stack

Y = 0
X = 1

class Maze:

    def __init__(self, archivo):

        def load_matrix():

            maze_matrix = []

            with open(f"laberintos/{archivo}", "r") as maze:

                len_prev_row = None

                while (row := maze.readline()) != "":

                    assert len_prev_row in [len(row), None], "La matriz del archivo no tiene una dimension correcta"
                    len_prev_row = len(row)

                    row_matrix = []
                    for char in row:
                        match char:
                            case "X":
                                row_matrix.append("X")
                            case ".":
                                row_matrix.append(".")
                            case "\n":
                                pass
                            case _:
                                raise Exception("El archivo seleccionado contiene caracteres no esperados")

                    maze_matrix.append(row_matrix)

            assert maze_matrix[0][0] == maze_matrix[-1][-1] == ".",\
                "las casillas iniciales y finales no pueden estar bloqueadas"

            return maze_matrix

        self.maze_matrix = load_matrix()
        self.__start_poss = (0,0)
        self.__n_rows = len(self.maze_matrix)
        self.__n_cols = len(self.maze_matrix[0])
        self.__end_poss = (self.__n_rows - 1, self.__n_cols - 1)
        self.patch = None



    def find_path(self):
        pass
        maze_copy = deepcopy(self.maze_matrix)

        stack = Stack()
        stack.push(self.__start_poss)

        while len(stack) != 0 and stack.peek() != self.__end_poss:

            y_current = stack.peek()[0]
            x_current = stack.peek()[1]


            new_positions = [
                (y_current - 1, x_current),     #Arriba
                (y_current, x_current + 1),     #Derecha
                (y_current + 1, x_current),     #Abajo
                (y_current, x_current - 1)      #Izquierda
            ]

            posible_move = False

            for position in new_positions:
                if (position[Y] % self.__n_rows == position[Y] and
                        position[X] % self.__n_cols == position[X] and
                        maze_copy[position[Y]][position[X]] == "."):
                    stack.push((position[Y], position[X]))
                    posible_move = True
                    break

            if not posible_move:
                stack.pop()

            maze_copy[y_current][x_current] = "V"

        self.__patch = stack
        return bool(len(stack))

    def show_path(self):

        maze_copy = deepcopy(self.maze_matrix)

        for i in range(self.__n_rows):
            for j in range(self.__n_cols):
                if (i, j) in self.__patch:
                    print("*", end="")
                else:
                    print(maze_copy[i][j], end="")
            print("")

def main():
    maze = Maze("prueba.txt")
    maze.find_path()
    maze.show_path()

if __name__ == "__main__":
    main()