
def factor(valor:int) -> int:
    if valor == 0:
        return 1
    else:
        return valor * factor(valor - 1)

def sum_list(list:list) -> int:
    if len(list) == 0:
        return 0
    else:
        return list[0]+sum_list(list[1:])

def invert_string(string:str) -> str:
    string = list(string)
    if len(string) == 1:
        return string[0]
    elif len(string) == 2:
        return "".join([string[1], string[0]])
    else:
        return "".join([string[-1], invert_string(string[1:-1]), string[0]])

def poupanca(invest:float, goal:float, bank:float= 0) -> int:

    if bank >= goal:
        return 1
    else:
        bank = bank*1.05 + invest
        return 1 + poupanca(invest,goal,bank=bank)

def bitcoin(valor, mes) -> int:
    pass

def juros_compostos(valor) -> int:
    pass