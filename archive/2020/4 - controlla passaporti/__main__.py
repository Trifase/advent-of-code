input = open("4.txt").read().strip()
passport_lines = []

partial_line = ""
for line in input.splitlines():
    if len(line) == 0:
        passport_lines.append(partial_line)
        partial_line = ""
    else:
        partial_line += line.strip() + " "
passport_lines.append(partial_line)


passports = []
for line in passport_lines:
    passport = dict([ kv.split(":") for kv in line.strip().split(" ") ])
    passports.append(passport)
# print(passports)
def check_valid_passport(passport: dict):
    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    if set(passport.keys()) != fields and set(passport.keys()) != (fields-{"cid"}):
        return False
    if not 1920 <= int(passport["byr"]) <= 2002:
        return False
    if not 2010 <= int(passport["iyr"]) <= 2020:
        return False
    if not 2020 <= int(passport["eyr"]) <= 2030:
        return False
    if not passport["hgt"].endswith("cm") and not passport["hgt"].endswith("in"):
        return False
    if passport["hgt"].endswith("cm") and not 150 <= int(passport["hgt"].replace("cm", "")) <= 193:
        return False
    if passport["hgt"].endswith("in") and not 59 <= int(passport["hgt"].replace("in", "")) <= 76:
        return False
    if not passport["hcl"].startswith("#") or not 0 <= int(passport["hcl"].replace("#", "0x"), 16) <= 0xffffff:
        return False
    if not passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False
    if not len(passport["pid"]) == 9 or not passport["pid"].isnumeric():
        return False
    return True
validati = sum([1 if check_valid_passport(passport) else 0 for passport in passports])
print(f'Il numero di passaporti validati da algoritmo ZIP ARGON è: {validati}')