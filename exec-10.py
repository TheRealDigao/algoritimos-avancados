#10) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.

custo_fabrica = float(input("Qual é o preço de fábrica? "))
percentual_distribuidor = 0.28
percentual_impostos = 0.45

custo_distribuidor = custo_fabrica*percentual_distribuidor
custo_impostos = custo_fabrica*percentual_impostos
custo_final = custo_fabrica+custo_distribuidor+custo_impostos

print(f"O custo final do consumidor é: R${custo_final:.2f}")
