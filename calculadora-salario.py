# Leitura dos dados
numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Exibição do resultado
print("Número =", numero_funcionario)
print(f"Salário = R$ {salario:.2f}")
