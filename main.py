import numpy as np

menemonicDic = {"JP": 0, "RS": 0, "JZ": 1, "JN": 2, "HJ": 3, "AD": 4, "SB": 5,
                "ML": 6, "DV": 7, "LD": 8, "ST": 9, "SC": 10, "GD": 11, "PD": 12,
                "OS": 13}

memory = [0 for n in range(4095)]
ci = 0
ac = 0
def getOp(instruction):
    op = instruction >> 12
    operand = instruction % 4096

    return op, operand

def stringBitToInt(string):
    return int(string, base=2)

def twos_comp(s):
    """compute the 2's complement of int value val"""
    val = int(s, base=2)
    if (val & (1 << 15)) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << 16)        # compute negative value
    return val

def returnInt16bit(num):
    return num % 65536
def cpuProcess(instruction):
    global memory
    global ci
    global ac

    op, operand = getOp(instruction)

    if op == 0:
        ci = operand
    elif op == 1:
        if ac == 0:
            ci = op
        else:
            ci += 1
    elif op == 2:
        if ac < 0:
            ci = op
        else:
            ci += 1
    elif op == 3:
        ci = op
    elif op == 4:
        ac = returnInt16bit(ac + memory[operand])
        ci += 1
    elif op == 5:
        ac = returnInt16bit(ac - memory[operand])
        ci += 1
    elif op == 6:
        ac = returnInt16bit(ac * memory[operand])
        ci += 1
    elif op == 7:
        ac = returnInt16bit(ac // memory[operand])
        ci += 1
    elif op == 8:
        ac = memory[operand]
        ci += 1
    elif op == 9:
        memory[operand] = ac
        ci += 1
    elif op == 10:
        memory[operand] = ci + 1
        ci = operand + 1
    elif op == 11:
        b = input("Digite em binario sua instrucao (16 bits): ")
        ac = twos_comp(b)
    elif op == 12:
        print("Acumulador: ")
        print("inteiro: {}".format(ac))
        print("binario: {}".format(format(ac, 'b')))
    elif op == 13:
        print("a ser implementado")


def main():
    # global definitions
    global memory
    global ci
    global ac

    # code execution
    print(getOp(int("1001000000000001", 2)))

main()
