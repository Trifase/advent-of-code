import re
from rich import print
import copy

# Utilities
def rematch(pattern, string):
    return re.fullmatch(pattern, string)

def lista(lista):
    for i in lista:
        print(i)

def list_to_string(lista):
    string = ''.join(str(x) for x in lista)
    return string

def string_to_list(string):
    lista = [ c for c in string ]
    return lista

def dec_to_bin(dec,bit):
    b = str(bin(int(dec))[2:]).zfill(bit)
    return b

def bin_to_dec(string,bit):
        dec = int(string, bit)
        return dec

def removeduplicates(lista):
  return list(dict.fromkeys(lista))

def list_replace(lst, old="1", new="10"):
    """replace list elements (inplace)"""
    i = -1
    try:
        while 1:
            i = lst.index(old, i + 1)
            lst[i] = new
    except ValueError:
        pass

# Parsing
FILENAME = "inputs/04.txt"
# FILENAME = "inputs/04-tommaso-amici.txt"
# FILENAME = "inputs/04-test.txt"

extractions = open(FILENAME).readlines()[0].strip().split(",")
lista_boards = [l.strip() for l in open(FILENAME).readlines()][2:]

bingo_boards: list = []
bingo_board = []
for riga in lista_boards:
    if riga != "":
        bingo_board.append(riga.split())
    else:
        bingo_boards.append(bingo_board)
        bingo_board = []


def mark_number_single_board(board: list[list], number) -> list:
    marked_board = []
    for row in board:
        list_replace(row, number, f"({number})")
        marked_board.append(row)
    return marked_board

def mark_numbers_all_boards(all_boards, number):
    marked_all_boards = []
    for board in all_boards:
        marked_board = mark_number_single_board(board, number)
        marked_all_boards.append(marked_board)
    return marked_all_boards

def check_if_board_won(board: list[list]) -> bool:

    def check_row(board: list[list]) -> bool:
        for row in board:
            if all(x.startswith("(") for x in row):
                return True
        return False

    def check_col(board: list[list]) -> bool:
        for i in range(5):
            col = [x[i] for x in board]
            if all(x.startswith("(") for x in col):
                return True
        return False

    if check_row(board) or check_col(board):
        return True
    return False

def sum_unmaked_cells(board : list[list]) -> int:
    result = 0
    for row in board:
        for cell in row:
            if not cell.startswith("("):
                result += int(cell)
    return result


# Part 1
sol1 = 0

winner = False
lastnumber = 0

for turno in range(len(extractions)):

    if winner:
        break

    numero = extractions[turno]
    bingo_boards = mark_numbers_all_boards(bingo_boards, numero)
    for board in bingo_boards:
        if check_if_board_won(board):
            winnerboard = copy.deepcopy(board)
            lastnumber = numero
            winner = True
            break

sol1 = int(lastnumber) * sum_unmaked_cells(winnerboard)

print(f"Parte 1: \t[{sol1}]")
print()


# Part 2
sol2 = 0

winner = False
lastnumber = 0

for turno in range(len(extractions)):

    # if winner:
    #     break

    numero = extractions[turno]
    bingo_boards = mark_numbers_all_boards(bingo_boards, numero)
    for board in bingo_boards:
        if check_if_board_won(board):
            winnerboard = copy.deepcopy(board)
            lastnumber = numero
            bingo_boards.remove(winnerboard)
            # break

sol2 = int(lastnumber) * sum_unmaked_cells(winnerboard)

print(f"Parte 2: \t[{sol2}]")

