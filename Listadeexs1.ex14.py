avista = float(input("Digite o valor do IPTU à vista: "))
parcelado =float(input("Digite o valor da parcela do IPTU: "))
aprazo = parcelado * 10
porcentual = 1- avista / aprazo

print ("O valor do desconto foi de: ", porcentual * 100, "%")
