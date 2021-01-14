import sys


def validate (field_name, field_value):
    if field_name not in fields:
        return False
    if field_name == "byr":
        if field_value.isnumeric():
            number = int(field_value)
            return 1920 <= number <= 2002
        else:
            return False
    elif field_name == "iyr":
        if field_value.isnumeric():
            number = int(field_value)
            return 2010 <= number <= 2020
        else:
            return False
    elif field_name == "eyr":
        if field_value.isnumeric():
            number = int(field_value)
            return 2020 <= number <= 2030
        else:
            return False
    elif field_name == "hgt":
        if field_value.endswith("cm"):
            number = field_value[0:field_value.index("cm")]
            if number.isnumeric():
                return 150 <= int(number) <= 193
            else:
                return False
        elif field_value.endswith("in"):
            number = field_value[0:field_value.index("in")]
            if number.isnumeric():
                return 59 <= int(number) <= 76
            else:
                return False
        else:
            return False
    elif field_name == "hcl":
        if field_value[0] == '#':
            valid = True
            for char in field_value:
                if char not in ['#','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
                    valid = False
                    break
            return valid
        else:
            return False
    elif field_name == "ecl":
        return field_value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field_name == "pid":
        return len(field_value) == 9 and field_value.isnumeric()
    else:
        return False

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
seen = [0, 0, 0, 0, 0, 0, 0]
valid_results = [0, 0, 0, 0, 0, 0, 0]

filename = open(sys.argv[1], 'r')
valid_counter = 0
passport_counter = 0
for line in filename.readlines():
    if line == '\n' or line == '\r\n':
        passport_counter += 1
        invalid = 0 in seen
        print("Passport " + str(passport_counter))
        print("Valid fields")
        print(valid_results)
        print("Seen")
        print(seen)
        print("\n")
        if (not invalid) and (0 not in valid_results):
            valid_counter += 1
        seen = [0, 0, 0, 0, 0, 0, 0]
        valid_results = [0, 0, 0, 0, 0, 0, 0]
        continue

    sections = line.split(" ")
    for section in sections:
        lhs, rhs = section.split(":")
        valid_field = validate(lhs.strip(), rhs.strip())
        if valid_field:
            valid_results[fields.index(lhs)] = 1
    
    for index in range(7):
        if fields[index] in line:
            seen[index] = 1

print(valid_counter)
