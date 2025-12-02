input = open("7.txt").read().strip().splitlines()

def parse_line(line: str):
    line = line[:-1] # remove last dot
    parts = line.split(" ", 4)
    from_bag = " ".join(parts[0:2])
    if parts[4] == "no other bags":
        to_bags = None
    else:
        to_bags_parts = parts[4].split(",")
        to_bags_parts = map(lambda p: p.replace("bags", "").replace("bag", "").strip(), to_bags_parts)
        to_bags = [
            to_bag_part.split(" ",1) for to_bag_part in to_bags_parts
        ]
        to_bags = [
            [int(n), color] for n, color in to_bags
        ]
    return from_bag, to_bags
# print(parse_line("light red bags contain 1 bright white bag, 2 muted yellow bags."))
# => ('light red', [[1, 'bright white'], [2, 'muted yellow']])

# for part 1
def eventually_contain_shiny_gold_bag(bags: dict, bag: str):
    if bags[bag] is None: # bag without bags
        return False

    contained_bags = list(map(lambda b: b[1], bags[bag])) # just need the color, not the quantity
    if 'shiny gold' in contained_bags: # bag with shiny gold
        return True

    return any(map(lambda bag: eventually_contain_shiny_gold_bag(bags, bag), contained_bags))

bags = dict(map(parse_line, input))
# bags => {'light red': [[1, 'bright white'], [2, 'muted yellow']], 'dark orange': [[3, 'bright white'], [4, 'muted yellow']], 'bright white': [[1, 'shiny gold']], 'muted yellow': [[2, 'shiny gold'], [9, 'faded blue']], 'shiny gold': [[1, 'dark olive'], [2, 'vibrant plum']], 'dark olive': [[3, 'faded blue'], [4, 'dotted black']], 'vibrant plum': [[5, 'faded blue'], [6, 'dotted black']], 'faded blue': None, 'dotted black': None}
print(bags)
# part 1
count = 0
for bag in bags:
    if eventually_contain_shiny_gold_bag(bags, bag):
        count += 1
print(count)

# for part 2
def count_subbags(bags: dict, bag: str):
    total = 0
    # if a bag has no other bags, 0
    if not bags[bag]:
        return 0
    for subbag_count, subbag_color in bags[bag]:
        total += subbag_count + subbag_count*count_subbags(bags, subbag_color)
    return total

print(count_subbags(bags, "shiny gold"))