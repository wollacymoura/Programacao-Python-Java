salario = float(input("Digite o seu salário: "))
aumento = float(input("Digite o seu aumento percentual anual: "))
tempo = int(input("Digite a quantidade de anos que você deseja saber o aumento total daquela época: "))

salario_atual = salario

for i in range(tempo):
    salario_atual *= 1 + (aumento / 100)
    aumento *= 2

print(int(salario_atual))