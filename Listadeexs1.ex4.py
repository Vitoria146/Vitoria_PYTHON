#nova forma de imprimir 
#print(f"{num_a} + {num_b} = {soma}")

aux = input ("Digite um número, a: ")
num_a = int(aux)
aux = input ("Digite um número, b: ")
num_b = int(aux)

soma = num_a + num_b
print(f"{num_a} + {num_b} = {soma}")
    
produto = num_a * num_b
print(f"{num_a} * {num_b} = {produto}")    

divisao = num_a // num_b
print(f"{num_a} // {num_b} = {divisao}")

resto = num_a % num_b
print(f"{num_a} % {num_b} = {resto}")