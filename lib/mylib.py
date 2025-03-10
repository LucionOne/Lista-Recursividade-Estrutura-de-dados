
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

def juros_compostos(amount:float, goal:float|list[float], bank:float=0) -> int:
    if type(goal) == float or type(goal) == int:
            goal_0 = goal
            goal_type = False
    else:
        try:
            goal_0 = goal[0]
            goal_type = True
        except:
            raise IndexError('Valores Limitados para ações/crypto')

    bank += amount

    if bank >= goal_0:
        return 1

    else:
        if goal_type:
            return 1 + juros_compostos(amount,goal[1:],bank=bank)
        else:
            return 1 + juros_compostos(amount,goal,bank=bank)

def month_to_time(time_month:int) -> tuple[int]:
    time_year = time_month//12
    time_month = time_month - time_year*12
    return (time_year, time_month)

def print_date(time_year:int, time_month:int) -> None:
    month_str = 'mês' if time_month**2 == 1 else 'meses'
    year_str = 'ano' if time_year**2 == 1 else 'anos'
    
    if time_year != 0:
        print(f'{time_year}',f'{year_str}')
    if time_month != 0:
        print(f'{time_month}',f'{month_str}')








