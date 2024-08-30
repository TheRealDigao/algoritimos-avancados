#8) Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

eleitores = int(input("Qual é o número total de eleitores? "))
brancos = int(input("Qual a quantidade de votos em branco? "))
nulos = int(input("Nulos? "))
validos = int(input("Válidos? "))

percentual_brancos = (brancos/eleitores)*100
percentual_nulos = (nulos/eleitores)*100
percentual_validos = (validos/eleitores)*100

print("- Total de porcentagens -")
print("- Total de votos em branco: ", percentual_brancos, "% -")
print("- Total de votos nulos: ", percentual_nulos, "% -")
print("- Total de votos válidos: ", percentual_validos, "% -")
