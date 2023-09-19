from board import Board
from player import Player
import game_logic


def check_int(__input__):
    for i in str(__input__):
        if i not in '0123456789':
            return False
        else:
            return True


def check_selected_square(selected):
    if not check_int(selected) or not 1 <= int(selected) <= size**2:
        print("Neplatny vstup. Zvol cislo volneho pole.")
        return False
    elif int(selected) in player_x or int(selected) in player_o:
        print("Pole obsazeno. Zkus to znovu.")
        return False
    else:
        return True


if input("Zadej pismena PC pro hru proti pocitaci, \nzadej cokoli jineho pro hru dvou hracu: ").upper() == 'PC':
    ap = [0, 2]
else:
    ap = [0, 1]
size = input("Zvol velikost od 3 do 9: ")
size_ok = False
while not size_ok:
    if not check_int(size) or int(size) < 3 or int(size) > 9:
        while not check_int(size) or int(size) < 3 or int(size) > 9:
            print("Neplatny vstup. Musi byt cislo od 3 do 9.")
            size = input("Zvol velikost: ")
    elif check_int(size) and 3 <= int(size) <= 9:
        size = int(size)
        size_ok = True
board = Board(size)
victory = False
moves = 0
player_o = []
player_x = []
num = 0
board.render(player_o, player_x)
while not victory:
    active_player = Player(ap[num])
    if ap[num] == 0:
        selected_square = active_player.getinput()
        if not check_selected_square(selected_square):
            num = 0
            print(moves)
        else:
            player_o.append(int(selected_square))
            moves += 1
            num = 1
        if game_logic.check_win(size, player_o):
            print("Vyhra!")
            victory = True
    elif ap[num] == 1:
        selected_square = active_player.getinput()
        if not check_selected_square(selected_square):
            num = 1
            print(moves)
        else:
            player_x.append(int(selected_square))
            moves += 1
            num = 0
        if game_logic.check_win(size, player_x):
            print("Vyhra!")
            victory = True
    elif ap[num] == 2:
        if len(player_o) > len(player_x):
            selected_square = game_logic.decide(size, player_x, player_o)
            player_x.append(selected_square)
            if game_logic.check_win(size, player_x):
                print("Vyhra!")
                victory = True
            moves += 1
            num = 0
    board.render(player_o, player_x)
    if moves == size**2 and not victory:
        print("Remiza.")
        break
