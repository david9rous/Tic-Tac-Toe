class Board:
    def __init__(self, size):
        self.size = size

    def render(self, player_o, player_x):
        size = self.size
        board_width = 1 + size * 6
        border = '#'
        for i in range(board_width):
            print(border, end='')
        print()
        for cell_y in range(1, size**2, size):
            for y in range(6):
                print(border, end='')
                for cell_x in range(size):
                    cell_number = cell_y + cell_x
                    cell = [
                        [cell_number, ' ', ' ', ' ', ' ', '#', ],
                        [' ', ' ', ' ', ' ', ' ', '#', ],
                        [' ', ' ', ' ', ' ', ' ', '#', ],
                        [' ', ' ', ' ', ' ', ' ', '#', ],
                        [' ', ' ', ' ', ' ', ' ', '#', ],
                        ['#', '#', '#', '#', '#', '#', ],
                    ]
                    if cell_number > 9:
                        cell[0].pop(-2)
                    o_cell = [
                        [cell_number, ' ', ' ', ' ', ' ', '#', ],
                        [' ', ' ', '-', ' ', ' ', '#', ],
                        [' ', '(', ' ', ')', ' ', '#', ],
                        [' ', ' ', '-', ' ', ' ', '#', ],
                        [' ', ' ', ' ', ' ', ' ', '#', ],
                        ['#', '#', '#', '#', '#', '#', ],
                    ]
                    if cell_number > 9:
                        o_cell[0].pop(-2)
                    x_cell = [
                        [cell_number, ' ', ' ', ' ', ' ', '#', ],
                        [' ', '\\', ' ', '/', ' ', '#', ],
                        [' ', ' ', 'x', ' ', ' ', '#', ],
                        [' ', '/', ' ', '\\', ' ', '#', ],
                        [' ', ' ', ' ', ' ', ' ', '#', ],
                        ['#', '#', '#', '#', '#', '#', ],
                    ]
                    if cell_number > 9:
                        x_cell[0].pop(-2)
                    for x in range(len(cell[y])):
                        if cell_number in player_x:
                            print(x_cell[y][x], end='')
                        elif cell_number in player_o:
                            print(o_cell[y][x], end='')
                        else:
                            print(cell[y][x], end='')
                print()
