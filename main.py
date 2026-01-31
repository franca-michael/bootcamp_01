CONSTANTE = 1_000


#solicite ao usuário que digite seu nome
nome = input("Por favor, digite seu nome: ")

#solicite ao usuário que digite o valor do seu salário
salario = float(input("Por favor, digite o valor do seu salário: "))

#solicite ao usuário que o digite o valor do bonus recebido
bonus = float(input("Por favor, digite o valor do bônus recebido: "))

#calcule o valor do bonus final

valor_bonus = CONSTANTE + (salario * bonus)

#imprima o cálculo de kpi para o usuário 
print(f"O valor do bônus final é: {valor_bonus}")

#imprima uma mensagem personalizada para o usuário com seu nome e o valor do bônus final
print(f"Olá, {nome}! O valor do seu bônus final é: {valor_bonus}")