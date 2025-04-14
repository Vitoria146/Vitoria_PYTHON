num = int(input("Digite um número: "))
#input serve para já para transformar o número em inteiro?
dez = num // 10
uni = num % 10

print('Dezena: ', dez)
print("Unidade: ", uni)

print(f"Dezena = {dez}")
print(f"Unidade = {uni}")
# f string, para colocar uma variável dentro dele para ser impressa