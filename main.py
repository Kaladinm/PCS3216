import numpy as np

menemonicDic = {"JP": 0, "RS": 0, "JZ": 1, "JN": 2, "HJ": 3, "AD": 4, "SB": 5,
                "ML": 6, "DV": 7, "LD": 8, "ST": 9, "SC": 10, "GD": 11, "PD": 12,
                "OS": 13}

memory = [0 for n in range(4095)]
ci = 0
ac = 0
run = False
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
    global run

    op, operand = getOp(instruction)
    print("EX: ci: {} instruction: {} {}".format(ci, op, operand))

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
        run = False
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
        print("Acumulador: ")
        print("inteiro: {}".format(ac))
        print("binario: {}".format(format(ac, 'b')))
    elif op == 12:
        b = input("Digite em binario seu valor pro ac (16 bits): ")
        ac = twos_comp(b)
        ci += 1
    elif op == 13:
        print("a ser implementado")


def main():
    # global definitions
    global memory
    global ci
    global ac
    global run

    # code execution
    while True:
        inp = int(input("1- Rodar código\n2-Escrever Instruçao\n3- Rodar Arquivo de texto\n4-Print Memoria\n5-Sair\n".format(ci)))
        if inp == 1:
            run = True
            ci_in = int(input("Escolha o ci para comecar a rodar(atual ci={}): ".format(ci)))
            ci = ci_in
            print("EXECUTING...")
            while run:
                cpuProcess(memory[ci])
            print("EXEC ENDED")
        elif inp == 2:
            mem_pos = int(input("Digite a posiçao de memoria(decimal): "))
            inst = input("Digite a instrução(binário): ")
            inst_int = stringBitToInt(inst)
            memory[mem_pos] = inst_int
        elif inp == 3:
            print("a ser feito")
        elif inp == 4:
            print(memory)
        else:
            break


main()
