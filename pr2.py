import sys

filename = open(sys.argv[1], 'r')
content = filename.read().splitlines()

correct = 0

for line in content:
    sections = line.split(": ")
    policy_sections = sections[0].split(" ")
    policy_letter = policy_sections[1]
    policy_params = policy_sections[0].split("-")
    pmin = int(policy_params[0]) - 1
    pmax = int(policy_params[1]) - 1

    password = sections[1]
    
    if pmin > len(password) - 1 or pmax > len(password) - 1:
        continue
    position1 = password[pmin] == policy_letter
    position2 = password[pmax] == policy_letter

    valid = position1 ^ position2
    print (line)
    print(valid)
    if valid:
        correct += 1

print(correct)
    