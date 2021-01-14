import sys

filename = open(sys.argv[1], 'r')
content = filename.read().splitlines()

possible_terms = []
visited_terms = []
visited = []
possible_count = 0

current_term = "shiny gold"
bag_count = 0

def clean_right(input_string):
    if input_string[0].isnumeric():
        count = int(input_string[0])
        remainder = input_string[2:]
        if count > 1:
            remainder = remainder.rstrip(" bags")
        elif count == 1:
            remainder = remainder.rstrip(" bag")
        else:
            print("not a known digit")
        return remainder
    print("invalid rule")
    return ''
        

def search_rules(term):
    if term not in visited_terms:
        visited_terms.append(term)
        for line in content:
            if term not in line.rstrip("."):
                continue
            lhs, rhs = line.rstrip(".").split(" contain ")
            clean_left = lhs.rstrip("bags").rstrip()
            
            for rule in rhs.rstrip().split(", "):
                if term not in rule:
                    continue
                else:
                    possible_terms.append(clean_left)
                    for x in possible_terms:
                        search_rules(x)

def count_bags(term) -> int:
    bag_count = 0
    for line in content:
        if term not in line.rstrip("."):
            continue
        lhs, rhs = line.rstrip(".").split(" contain ")
        if term in lhs:
            for t in rhs.rstrip().split(", "):
                count = 0
                space_index = t.index(" ")
                if t[:space_index].isnumeric():
                    count = int(t[:space_index])
                    bag_count += count
                    parsed = t[space_index+1:]
                    if count > 1:
                        parsed = parsed.rstrip(" bags")
                    elif count == 1:
                        parsed = parsed.rstrip(" bag")
                    else:
                        break
                    bag_count += count * count_bags(parsed)
    
    print(term, bag_count)
    return bag_count

                

search_rules(current_term)
bag_count = count_bags(current_term)

print(len(set(possible_terms)))
print(bag_count)