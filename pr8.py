import sys

executed = []
accumulator = 0
latest_jump = 0

def execute_from(line):
    global accumulator
    if (executed[line] == 1):
        print("Already executed", line)
        print("Accumulator", accumulator)
        return
    if content[line][:3] == "nop":
        executed[line] = 1
        execute_from(line+1)
    if content[line][:3] == "acc":
        executed[line] = 1 
        operand = content[line][4:]
        add_result = 0
        if operand[0] == '+':
            add_result += int(operand[1:])
        elif operand[0] == '-':
            add_result -= int(operand[1:])
        accumulator += int(add_result)
        execute_from(line+1)
    if content[line][:3] == "jmp":
        executed[line] = 1
        operand = content[line][4:]
        jump_result = 0
        if operand[0] == '+':
            jump_result += int(operand[1:])
        elif operand[0] == '-':
            jump_result -= int(operand[1:])
        execute_from(line+jump_result)


filename = open(sys.argv[1], 'r')
content = filename.read().splitlines()

for line in content:
    executed.append(0)


execute_from_p2(0)