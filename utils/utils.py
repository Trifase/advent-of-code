import os
import os.path
import re
import sys

import requests
from dataclassy import dataclass

from .sessions import SESSIONS

# 2022 Day 13
def remove_empty_from_data(lista: list[str]) -> list[str]:
    newlist = []
    for element in lista:
        if element:
            newlist.append(element)
    return newlist


@dataclass
class MovingThing:
    """
    This is the base class of a moving thing in a 2D matrix.
    It has two coords (x and y) and a move() function that takes
    a direction ((L)eft, (R)ight, (U)p and (D)own) and optionally an amount.
    It has a move_to() to move the point to new coords.
    You can mode like this:

    point.move_to((3,6))

    point.coords = 3,6

    point.x = 3
    point.y = 6
    """

    x: int = 0
    y: int = 0

    dir: str = "N"

    heading: int = 0

    @property
    def coords(self):
        return (self.y, self.x)

    @property
    def coords_grid(self):
        return (self.x, self.y)

    @property
    def look_ahead(self):
        match self.dir:
            case "N":
                return (self.y - 1, self.x)
            case "S":
                return (self.y + 1, self.x)
            case "E":
                return (self.y, self.x + 1)
            case "W":
                return (self.y, self.x - 1)


    @coords.setter
    def coords(self, coords):
        self.x = coords[1]
        self.y = coords[0]

    def turn(self, dir: str):
        dirs = ["N", "E", "S", "W"]
        curr_dir = dirs.index(self.dir)
        if dir == "R":
            self.dir = dirs[(curr_dir + 1) % 4]
        elif dir == "L":
            self.dir = dirs[(curr_dir - 1) % 4]

    def go(self, units: int = 1):
        match self.dir:
            case "N":
                self.y -= units
            case "S":
                self.y += units
            case "E":
                self.x += units
            case "W":
                self.x -= units

    def move(self, dir: str, units: int = 1):
        match dir:
            case "U":
                self.y += units
            case "D":
                self.y -= units
            case "R":
                self.x += units
            case "L":
                self.x -= units
        self.coords = (self.x, self.y)

    def grid_move(self, dir: str, units: int = 1):
        print(f"[GRID] {dir} {units}")
        match dir:
            case "U":
                self.y -= units
            case "N":
                self.y -= units
            case "D":
                self.y += units
            case "S":
                self.y += units
            case "R":
                self.x += units
            case "E":
                self.x += units
            case "L":
                self.x -= units
            case "W":
                self.x -= units
        self.coords = (self.y, self.x)

    def move_to(self, coords: tuple[int, int]):
        self.x = coords[0]
        self.y = coords[1]

    def __repr__(self):
        return f"MovingThing y={self.y}, x={self.x} dir={self.dir}"


def rematch(pattern, string):
    return re.fullmatch(pattern, string)


def split_in_chunks(lst, length):
    for i in range(0, len(lst), length):
        yield lst[i : i + length]


def get_data(year, day, sessions=None, strip=True, integers=False, example=False):
    #Overwriting sessions with the one in the file
    sessions = SESSIONS
    USER_AGENT = "github.com/Trifase by luca.bellanti@gmail.com"

    if not os.path.isfile(f"inputs/{year}-{day}-example.txt"):
        open(f"inputs/{year}-{day}-example.txt", "w").close()

    if not os.path.isfile(f"inputs/{year}-{day}.txt"):
        url = f"https://adventofcode.com/{str(year)}/day/{str(day)}/input"
        headers = {
            "Cookie": f"session={sessions}",
            "User-Agent": USER_AGENT,
        }
        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            with open(f"inputs/{year}-{day}.txt", "w") as file:
                file.write(r.text)
        else:
            sys.exit(f"/api/alerts response: {r.status_code}: {r.reason} \n{r.content}")

    if example:
        data = open(f"inputs/{year}-{day}-example.txt", "r")
    else:
        data = open(f"inputs/{year}-{day}.txt", "r")

    if integers:
        return [int(line.strip()) if strip else int(line) for line in data.readlines()]
    else:
        return [line.strip() if strip else line for line in data.readlines()]


def get_data_from_file(file_url, strip=True, integers=False):
    data = open(f"{file_url}", "r")

    if integers:
        return [int(line.strip()) if strip else int(line) for line in data.readlines()]
    else:
        return [line.strip() if strip else line for line in data.readlines()]


def split_list(list):
    _list = []
    for y in "\n".join(list).split("\n\n"):
        _list.append([x for x in y.split("\n")])
    return _list


def sliding_window(lista: list, length: int) -> list:
    for i in range(0, len(lista) - length + 1):
        yield lista[i : i + length]


def make_grid(data: list[str]) -> list[list[str]]:
    return [list(line) for line in data]


def get_neighbors(coords: tuple[int, int], grid: list[str], diagonals: bool = False, return_values: bool = False, return_dict: bool = False) -> list[tuple[int, int]] | dict[tuple[int,int], str] | list[str]:
    y, x = coords
    y_max = len(grid)
    x_max = len(grid[0])
    if return_dict:
        return_values = False

    su = (y - 1, x) if y != 0 else None
    dx = (y, x + 1) if x != x_max - 1 else None
    giu = (y + 1, x) if y != y_max - 1 else None
    sx = (y, x - 1) if x != 0 else None

    if diagonals:
        su_dx = (y - 1, x + 1) if y != 0 and x != x_max - 1 else None
        giu_dx = (y + 1, x + 1) if y != y_max - 1 and x != x_max - 1 else None
        giu_sx = (y + 1, x - 1) if y != y_max - 1 and x != 0 else None
        su_sx = (y - 1, x - 1) if y != 0 and x != 0 else None
        if return_values:
            availables = [t for t in [su, dx, giu, sx, su_dx, giu_dx, giu_sx, su_sx] if t]
            return [grid[y][x] for y, x in availables]
            # return [grid[y][x] for y, x in [su, dx, giu, sx, su_dx, giu_dx, giu_sx, su_sx] if y and x]
        return [t for t in [su, dx, giu, sx, su_dx, giu_dx, giu_sx, su_sx] if t]

    if return_values:
        print('v', [su, dx, giu, sx])
        return [grid[y][x] for y, x in [su, dx, giu, sx] if y and x]
    if return_dict:
        my_dict = {}
        if su:
            my_dict[su] = grid[su[0]][su[1]]
        if dx:
            my_dict[dx] = grid[dx[0]][dx[1]]
        if giu:
            my_dict[giu] = grid[giu[0]][giu[1]]
        if sx:
            my_dict[sx] = grid[sx[0]][sx[1]]
        return my_dict
    return [t for t in [su, dx, giu, sx] if t]
