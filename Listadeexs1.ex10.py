#Usain Bolt é o recordista mundial dos 100 metros rasos com o tempo de 9,58 segundos.
#Escreva um algoritmo que calcula a velocidade média em m/s e em km/h de um corredor,
#seu algoritmo recebe como dados de entrada a distância em metros e o tempo em segundos.

distancia = float(input("Distância em metros: " ))
tempo = float (input("Tempo em segundos: "))

velocidade = distancia / tempo
print(f"Velocidade: {velocidade} m/s")

dist_km = distancia / 1000
tempo_h = tempo / 3600
velocida_kmh = dist_km / tempo_h
print(f"ou  {velocida_kmh} km/h")