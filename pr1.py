import sys

filename = open(sys.argv[1], 'r')
content = filename.read().splitlines()

integer_content = [int(x) for x in content]

for x in integer_content:
    for y in integer_content:
        for z in integer_content:
            if x + y + z == 2020:
                print("x:", x)
                print("y:", y)
                print("z:", z)
                print(x*y*z)

    