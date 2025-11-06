# Exercício 1 – Faturamento diário
# Você tem um registro de vendas de uma loja durante a semana:
# faturamento = [
#  {"dia": "segunda", "valor": 1200},
#  {"dia": "terça", "valor": 1500},
#  {"dia": "quarta", "valor": 900},
#  {"dia": "quinta", "valor": 1800},
#  {"dia": "sexta", "valor": 2400},
# ]
# 1. Calcule o faturamento total da semana.
# 2. Descubra qual foi o dia de maior faturamento.
# 3. Calcule a média de vendas.

faturamento = [
 {"dia": "segunda", "valor": 1200},
 {"dia": "terça", "valor": 1500},
 {"dia": "quarta", "valor": 900},
 {"dia": "quinta", "valor": 1800},
 {"dia": "sexta", "valor": 2400},
]

total = 0
for valor in faturamento:
    total += valor["valor"]
print(total)

# Exercício 2 – Estoque de produtos
# Uma empresa tem o seguinte estoque:
# estoque = { # estoques em 3 filiais
#  "notebook": [5, 7, 3],  
#  "mouse": [20, 25, 18],
#  "teclado": [12, 14, 9],
# }
# 1. Calcule o estoque total de cada produto.
# 2. Descubra qual produto tem o menor estoque total.
# 3. Transforme os totais em um novo dicionário.

#1

estoque = { # estoques em 3 filiais
 "Notebook": [5, 7, 3],  
 "Mouse": [20, 25, 18],
 "Teclado": [12, 14, 9],
}

estoque_total = {}
for produto, quantidades in estoque.items():
    estoque_total[produto] = sum(quantidades)
print(estoque_total)

#2

menor_valor = None
produto_com_menor_estoque = None

for produto, total in estoque_total.items():
    if menor_valor is None or total < menor_valor:
        menor_valor = total
        produto_com_menor_estoque = produto

print(f"\nO produto com o menor estoque é o '{produto_com_menor_estoque}', com {menor_valor} unidades.")

#3

# Exercício 3 – Funcionários e salários
# Considere a lista de funcionários:
# funcionarios = [
#  {"nome": "Ana", "salario": 4500, "departamento": "RH"},
#  {"nome": "Carlos", "salario": 7000, "departamento": "TI"},
#  {"nome": "Beatriz", "salario": 5200, "departamento": "Financeiro"},
#  {"nome": "João", "salario": 4800, "departamento": "TI"},
# ]
# 1. Calcule a folha salarial total da empresa.
# 2. Descubra qual funcionário ganha mais.
# 3. Agrupe os salários por departamento em um dicionário.

#1

funcionarios = [
 {"nome": "Ana", "salario": 4500, "departamento": "RH"},
 {"nome": "Carlos", "salario": 7000, "departamento": "TI"},
 {"nome": "Beatriz", "salario": 5200, "departamento": "Financeiro"},
 {"nome": "João", "salario": 4800, "departamento": "TI"},
]

total = 0
for salario in funcionarios:
    total += salario["salario"]

print(total)

#2

funcionario_maior_salario = ""
maior_salario = 0

for funcionario in funcionarios:
    if funcionario["salario"] > maior_salario:
        maior_salario = funcionario["salario"]
        funcionario_maior_salario = funcionario["nome"]
    
print(f"O funcionário com o maior salário é: {funcionario_maior_salario} com o salário de: {maior_salario}")

#3

dep = {}

for funcionario in funcionarios:
    departamento = funcionario["departamento"]
    salario = funcionario["salario"]
    nome = funcionario["nome"]

    if departamento not in dep:
        dep[departamento] = {}
    dep[departamento][nome] = salario
print(dep)

# Exercício 4 – Pesquisa de satisfação
# Uma pesquisa coletou avaliações de clientes (0 a 10):
# avaliacoes = {
#  "loja A": [8, 9, 7, 10, 6],
#  "loja B": [5, 7, 6, 8, 7],
#  "loja C": [9, 8, 9, 10, 9],
# }
# 1. Calcule a média de satisfação de cada loja.
# 2. Descubra qual loja tem a maior média.
# 3. Gere um dicionário só com as médias.

avaliacoes = {
    "loja A": [8, 9, 7, 10, 6],
    "loja B": [5, 7, 6, 8, 7],
    "loja C": [9, 8, 9, 10, 9],
}

media_lojas = {}
for loja, notas in avaliacoes.items():
    soma = sum(notas)
    quantidade = len(notas)
    media = soma / quantidade
    media_lojas[loja] = media

print(f"Média de satisfação por loja: {media_lojas}")

maior = ""
media_maior = 0

for loja, media in media_lojas.items():
    if media > media_maior:
        media = media_maior
        loja = maior

print(f"A loja com a maior média é a {maior} com uma média de {media_maior}")

maior_media = 0
loja_maior_media = ""

for loja, media in media_lojas.items():
    if media > maior_media:
        maior_media = media
        loja_maior_media = loja

print(f"A loja com a maior média de satisfação é a '{loja_maior_media}', com uma média de {maior_media}.")