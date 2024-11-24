map = open("3.txt").read().strip().splitlines()

def slope(destra, giu):
    y = 0
    x = 0
    alberi = 0
    while y < (len(map)):
        if map[y][x%len(map[y])] == "#":
            alberi += 1
        x = x + destra
        y = y + giu
    return alberi

#Parte1
print(slope(3,1))

#Parte2
print(
    slope(3,1)*slope(1,1)*slope(5,1)*slope(7,1)*slope(1,2)
    )
print("###########")
print()

n_lines = 1
trees_pos = 4
n_trees = 0
with open("trees.txt") as trees:
    for line in trees:
        print(f'analizziamo: {line}')
        # if n_lines == 1:
        #     n_lines += 1
        #     continue
        # if n_lines > 1 and trees_pos == trees_pos:
        #     if line.find("#"[trees_pos -1]) == True:
        #         n_trees += 1
        #         trees_pos += 3
        #         print(trees_pos)
   # ~ n_lines += 1
  # ~ elif n_lines > 2 and trees_pos:
# print(n_trees)