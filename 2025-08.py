
import os
import math
import itertools

from icecream import ic
# from dataclassy import dataclass
from dataclasses import dataclass

import utils

# YEAR and DAY from the current file name YYYY-DD.
YEAR = int(os.path.basename(__file__).split(".")[0].split("-")[0])
DAY = int(os.path.basename(__file__).split(".")[0].split("-")[1])

# Used to overwrite the year and day
# YEAR = 2015
# DAY = 07

EXAMPLE = False
DEBUG = False

if DEBUG:
    ic.enable()
else:
    ic.disable()


def p(data: any) -> None:
    if DEBUG:
        print(data)


# Input parsing
print()


@utils.profiler(display_name="Opening.....DONE")
def get_input() -> any:
    """
    Get the input from the file or internet
    """
    data = utils.get_data(YEAR, DAY, strip=True, example=EXAMPLE)
    return data


@utils.profiler(display_name="Parsing.....DONE")
def parsing_input(data) -> any:
    """
    We'll do something with the input
    """

    return data

@dataclass
class CircuitBox:
    x: int = 0
    y: int = 0
    z: int = 0

    circuit: int = 0

    def distance_with(self, other: "CircuitBox") -> int:
        # sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2)
    
    def __repr__(self) -> str:
        c = f"[{self.circuit}] " if self.circuit != 0 else ""
        return f"{c}({self.x},{self.y},{self.z})"



# Part 1
@utils.profiler(display_name="Part 1......DONE")
def part1(data: any) -> int:
    sol1 = 0
    boxes = []
    for coord in data:
        x, y, z = map(int, coord.split(","))
        box = CircuitBox(x=x, y=y, z=z)
        boxes.append(box)

    # make all the pairings
    pairings = itertools.combinations(boxes, 2)

    MAX_PAIRINGS = 10
    if not EXAMPLE:
        MAX_PAIRINGS = 1000
    
    # p(f"Created {len(boxes)} boxes, total pairings: {len(list(pairings))}")

    # for each pairing calculate the distance, and take the first 10/1000 pairings with shorter distance
    distances = {}
    for box1, box2 in pairings:
        distance = box1.distance_with(box2)
        distances[distance] = (box1, box2)
    sorted_distances = dict(sorted(distances.items()))

    circuits = {}
    c = 1 # starting circuit number

    for i, (distance, (box1, box2)) in enumerate(sorted_distances.items()):
        if i < MAX_PAIRINGS:
            p(f"\nDistance: {distance} between Box1: {box1} and Box2: {box2}")
            if box1.circuit == 0 and box2.circuit == 0:
                box1.circuit = c
                box2.circuit = c
                circuits[c] = [box1, box2]
                p(f" → Assigned circuit {c} to boxes: {box1}, {box2}")
                c += 1
            elif box1.circuit != 0 and box2.circuit == 0:
                box2.circuit = box1.circuit
                circuits[box1.circuit].append(box2)
                p(f" → Assigned box2 {box2} to circuit {box1.circuit}")
            elif box1.circuit == 0 and box2.circuit != 0:
                box1.circuit = box2.circuit
                circuits[box2.circuit].append(box1)
                p(f" → Assigned box1 {box1} to circuit {box2.circuit}")
            elif box1.circuit != 0 and box2.circuit != 0:
                # merge the small circuit in the big one
                if box1.circuit != box2.circuit:
                    small_circuit = box2.circuit if len(circuits[box2.circuit]) < len(circuits[box1.circuit]) else box1.circuit
                    big_circuit = box1.circuit if small_circuit == box2.circuit else box2.circuit
                    # p(f" → Merging circuit {small_circuit} into circuit {big_circuit}")
                    for box in circuits[small_circuit]:
                        box.circuit = big_circuit
                        circuits[big_circuit].append(box)
                    del circuits[small_circuit]
        else:
            break # we don't care about the rest

    if DEBUG:
        p("Final circuits:")
        for circuit_id, boxes in circuits.items():
            p(f"\nCircuit {circuit_id}:")
            for box in boxes:
                p(f" - Box: {box}")

    # get the unique sizes of the circuits
    circuit_sizes = set([len(boxes) for boxes in circuits.values()])
    p(f"\nCircuit sizes: {circuit_sizes}")

    #multiply the sizes together
    sol1 = 1
    # multiply the three biggest sizes
    circuit_sizes = sorted(circuit_sizes, reverse=True)[:3]
    p(f"Top 3 circuit sizes: {circuit_sizes}")
    for size in circuit_sizes:
        sol1 *= size

    return sol1


# Part 2
@utils.profiler(display_name="Part 2......DONE")
def part2(data: any) -> int:
    sol2 = 0
    boxes = []
    for coord in data:
        x, y, z = map(int, coord.split(","))
        box = CircuitBox(x=x, y=y, z=z)
        boxes.append(box)


    # make all the pairings
    pairings = itertools.combinations(boxes, 2)

    # for each pairing calculate the distance, and take the first 10/1000 pairings with shorter distance
    distances = {}

    for box1, box2 in pairings:
        distance = box1.distance_with(box2)
        distances[distance] = (box1, box2)
    
    sorted_distances = dict(sorted(distances.items()))

    circuits = {}
    c = 1 # starting circuit number
    last_connected = None

    for _, (distance, (box1, box2)) in enumerate(sorted_distances.items()):
        p(f"\nDistance: {distance} between Box1: {box1} and Box2: {box2}")

        if box1.circuit == 0 and box2.circuit == 0:
            box1.circuit = c
            box2.circuit = c
            circuits[c] = [box1, box2]
            last_connected = [box1, box2]
            p(f" → Assigned circuit {c} to boxes: {box1}, {box2}")
            c += 1

        elif box1.circuit != 0 and box2.circuit == 0:
            box2.circuit = box1.circuit
            circuits[box1.circuit].append(box2)
            last_connected = [box1, box2]
            p(f" → Assigned box2 {box2} to circuit {box1.circuit}")

        elif box1.circuit == 0 and box2.circuit != 0:
            box1.circuit = box2.circuit
            circuits[box2.circuit].append(box1)
            last_connected = [box1, box2]
            p(f" → Assigned box1 {box1} to circuit {box2.circuit}")

        elif box1.circuit != 0 and box2.circuit != 0:
            # merge the small circuit in the big one
            if box1.circuit != box2.circuit:
                last_connected = [box1, box2]
                small_circuit = box2.circuit if len(circuits[box2.circuit]) < len(circuits[box1.circuit]) else box1.circuit
                big_circuit = box1.circuit if small_circuit == box2.circuit else box2.circuit
                p(f" → Merging circuit {small_circuit} into circuit {big_circuit}")
                for box in circuits[small_circuit]:
                    box.circuit = big_circuit
                    circuits[big_circuit].append(box)
                del circuits[small_circuit]

    if DEBUG:
        p("Final circuits:")
        for circuit_id, boxes in circuits.items():
            p(f"\nCircuit {circuit_id}:")
            for box in boxes:
                p(f" - Box: {box}")

    p(f"\nLast connected boxes: {last_connected}")

    #multiply the x coord together
    sol2 = last_connected[0].x * last_connected[1].x
    return sol2

s1 = 'Not run'
s2 = 'Not run'
data = get_input()
data = parsing_input(data)
s1 = part1(data)
s2 = part2(data)

print()
print(f"=========:: [DAY {DAY}] ::=========")
print(f"Soluzione Parte 1: [{s1}]")
print(f"Soluzione Parte 2: [{s2}]")
