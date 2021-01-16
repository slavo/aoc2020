import sys

filename = open(sys.argv[1], 'r')
content = filename.read().splitlines()
wrong_number = 0

def find_number(start_from):
    start_index = start_from - 25
    end_index = start_from
    previous_25 = [int(x) for x in content[start_index:end_index]]
    current_number = int(content[start_from])

    found = False
    for x, number1 in enumerate(previous_25):
        for y, number2 in enumerate(previous_25):
            if number1 == number2:
                continue
            if number1 + number2 == current_number:
                found = True
    
    return found

def find_weakness(number):
    numbers = [int(x) for x in content]
    for x in range(len(numbers) - 1):
        for y in range(x,len(numbers) - 1):
            if x == y:
                continue
            total = sum(numbers[x:y+1])
            if total == number:
                number1 = min(numbers[x:y+1])
                number2 = max(numbers[x:y+1])
                return number1 + number2
x = 25
while x < len(content):
    current = int(content[x])
    if not find_number(x):
        wrong_number = current
        break
    x += 1

print(wrong_number)
print("Weakness")
print(find_weakness(wrong_number))
