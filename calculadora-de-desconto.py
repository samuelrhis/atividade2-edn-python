# Informações do produto
nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

# Cálculo do desconto
valor_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibição dos detalhes
print("==== DETALHES DA COMPRA ====")
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {percentual_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")
