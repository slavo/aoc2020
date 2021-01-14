import sys, string

current_group = dict.fromkeys(string.ascii_lowercase, 0)
everyone = dict.fromkeys(string.ascii_lowercase, 0)

group_count = 0
sum_answers = 0
sum_everyone = 0
person_count = 0

filename = open(sys.argv[1], 'r')
for line in filename.readlines():
    if line == "\n":
        everyone_answers = len([1 for x in everyone.values() if x >= person_count])
        print(everyone)
        print(person_count)
        person_count = 0
        group_count += 1
        answers = len([x for x in current_group.values() if x == 1])
        current_group = dict.fromkeys(string.ascii_lowercase, 0)
        everyone = dict.fromkeys(string.ascii_lowercase, 0)
        sum_answers += answers
        sum_everyone += everyone_answers
    else:
        person_count += 1
        chars = line.strip()
        for c in chars:
            current_group[c] = 1
            everyone[c] += 1

print("part 1")
print(sum_answers)
print("part2")
print(sum_everyone)
