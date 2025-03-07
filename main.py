from lib import mylib

print()
print(mylib.factor(5))

print()
print(mylib.sum_list([29,30,6,4]))

print()
print(mylib.invert_string('WarHammer'))

print()
print(mylib.poupanca(1000,100000))
print()

btc_VALUES_2024 = ( 221787.06,
                    213144.52,
                    314880.80,
                    343092.00,
                    299365.18,
                    357068.67,
                    354521.00,
                    369989.88,
                    327315.34,
                    337335.00,
                    409895.99,
                    587000.00)
# vc pode adicionar qualquer lista/tuple de historico de valores de ações/crypto e de qualque tamanho
months = mylib.juros_compostos(250,100000)
time_tuple = mylib.month_to_time(months)
mylib.print_date(time_tuple[0],time_tuple[1])
print()
months_btc = mylib.juros_compostos(130000,btc_VALUES_2024)
time_tuple = mylib.month_to_time(months_btc)
mylib.print_date(time_tuple[0],time_tuple[1])
#ele levanta um erro se vc tem uma lista de valores de ações/crypto que não são o suficiente para atingir o objetivo
# print()
# months = mylib.juros_compostos(250,btc_VALUES_2024)
# time_tuple = mylib.month_to_time(months)
# mylib.print_date(time_tuple[0],time_tuple[1])
input()

