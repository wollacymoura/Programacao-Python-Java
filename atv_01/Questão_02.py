segundos = float(input("Digite a quantidade de segundos que deseja converter: "))
dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60 

print(f"{segundos} segundos, dá um total de {dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")