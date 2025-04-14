salarioA =float(input ("Informe o seu salário antes do aumento: "))
salarioB = float(input("Informe seu salário atual: "))

percentual = salarioB / salarioA - 1

print("O percentual do aumento do seu salário é de: ", percentual * 100, "%")