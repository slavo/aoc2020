import sys

filename = open(sys.argv[1], 'r')
content = filename.read().splitlines()
seat_numbers = [[0 for x in range(8)] for y in range(128)]

for line in content:
    rows = line[:7]
    columns = line[7:]

    current_low = 0
    current_high = 127
    for char in rows:
        if char == 'F':
            current_high -= ((current_high - current_low + 1) // 2)
        elif char == 'B':
            current_low += ((current_high - current_low + 1) // 2)
    row = current_low

    current_min = 0
    current_max = 7
    for char in columns:
        if char == 'L':
            current_max -= ((current_max - current_min + 1) // 2)
        elif char == 'R':
            current_min += ((current_max - current_min + 1) // 2)
    column = current_max

    seat_numbers[row][column] = 1

    seat_number = 8*row + column
    # print("Row", "Col")
    # print(row, column)
    # print(seat_number)
    # print('\n')

print(seat_numbers)

yours = 0

for row in seat_numbers:
    for column in row:
        if column == 0:
            #unoccupied
            column_index = row.index(column)
            row_index = seat_numbers.index(row)
            front = seat_numbers[row_index - 1][column_index] == 1
            back = seat_numbers[row_index + 1][column_index] == 1
            left = seat_numbers[row_index][column_index - 1] == 1
            right = seat_numbers[row_index][column_index + 1] == 1
            if (front and back and left and right):
                print("Found your seat")
                print(row_index, column_index)
                print(8*row_index + column_index)
