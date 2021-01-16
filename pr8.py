import sys

executed = []
accumulator = 0
latest_jump = 0

filename = open(sys.argv[1], 'r')
content = filename.read().splitlines()

# part 1 solution
def execute_from(instructions, line):
    global accumulator
    global executed
    #print("executing", line)
    if line >= len(instructions):
        return True
    if (instructions[line] == "\n"):
        return True
    if (executed[line] == 1):
        return False
    if instructions[line][:3] == "nop":
        executed[line] = 1
        return execute_from(instructions, line+1)
    if instructions[line][:3] == "acc":
        executed[line] = 1 
        operand = instructions[line][4:]
        add_result = 0
        if operand[0] == '+':
            add_result += int(operand[1:])
        elif operand[0] == '-':
            add_result -= int(operand[1:])
        accumulator += int(add_result)
        return execute_from(instructions, line+1)
    if instructions[line][:3] == "jmp":
        executed[line] = 1
        operand = instructions[line][4:]
        jump_result = 0
        if operand[0] == '+':
            jump_result += int(operand[1:])
        elif operand[0] == '-':
            jump_result -= int(operand[1:])
        return execute_from(instructions, line+jump_result)

def get_operand(line):
    operand = line[4:]
    if operand[0] in ['+', '-']:
        if operand[1:].isnumeric():
            return int(operand[1:])
    raise ValueError(line)


for idx, line in enumerate(content):
    modified_content = content.copy()
    instruction = line[0:3]
    if instruction == "acc":
        continue
    if instruction == "nop":
        new_instruction = line.replace("nop", "jmp")
        modified_content[idx] = new_instruction
    elif instruction == "jmp":
        new_instruction = line.replace("jmp", "nop")
        modified_content[idx] = new_instruction
    executed = [0 for x in modified_content]
    accumulator = 0
    #print(modified_content)
    result = execute_from(modified_content, 0)
    if result:
        print(accumulator)
    