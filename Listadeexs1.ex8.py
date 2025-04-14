#Uma pessoa tem em seu guarda roupa x camisas, y calças e z pares de sapato. Escreva
#um algoritmo que calcula de quantas maneiras diferentes ele pode se vestir. Seu algoritmo
#deverá ler o número de camisas, o número de calças e o número de pares de sapato.

aux = input ("Digite uma quantidade de camisas, x: ")
x = int(aux)
aux = input ("Digite uma quantidade de calças, y: ")
y = int(aux)
aux = input ("Digite uma quantidade de pares de sapato, z: ")
z = int(aux)

produto = x * y * z
print(f"Número de combinações = {produto}")    