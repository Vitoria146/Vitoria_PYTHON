# Lê o preço original do produto
preco = float(input("Digite o preço do produto: R$ "))

# Lê o percentual de alteração
percentual = float(input("Digite o percentual (%): "))

# Pergunta se é desconto ou aumento
tipo = input("É um desconto ou aumento? (digite 'desconto' ou 'aumento'): ").strip().lower()

# Calcula o valor da alteração e o novo preço
if tipo == "desconto":
    valor_alteracao = preco * (percentual / 100)
    novo_preco = preco - valor_alteracao
    print(f"Desconto de R$ {valor_alteracao:.2f}")
    print(f"Novo preço: R$ {novo_preco:.2f}")

elif tipo == "aumento":
    valor_alteracao = preco * (percentual / 100)
    novo_preco = preco + valor_alteracao
    print(f"Aumento de R$ {valor_alteracao:.2f}")
    print(f"Novo preço: R$ {novo_preco:.2f}")

else:
    print("Tipo inválido. Digite 'desconto' ou 'aumento'.")
