#9) Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

salario = float(input("Qual é o salário mensal do funcionário? "))
reajuste = float(input("Qual é o percentual de reajuste? "))

novo_salario = salario + (salario*(reajuste/100))

print(f"O novo salário é de R$ {novo_salario:.2f}")
