import sys

filename = open(sys.argv[1], 'r')
content = filename.read().splitlines()

horizontal_size = len(content[0])
vertical_size = len(content)

matrix = []
for line in content:
    newline = line
    for repetitions in range(5000):
        newline += line
    matrix.append(newline)

line_start = 0
tree_counter = 0
counter = 0
for line in matrix:
    print("line_start")
    counter += 1
    if counter % 2 == 0:
        print("skip")
        continue
    
    print(line_start)
    if line_start > len(line) - 1:
        print("Continue")
        continue
    if line[line_start] == '#':
        tree_counter += 1
    line_start += 1

print(tree_counter)