#Aluno

aluno = {"Nome": "Alberto",
        "Idade": 71,
        "Curso": "Direito"}

print(aluno['Nome'])
print(aluno['Idade'])
print(aluno['Curso'])

#Produto

produto = {
    "Nome": "Teclado Mecânico",
    "Preço": 350.00,
    "Estoque": 10}

produto["Marca"] = "Osklen"
produto["Preço"] = 320.00
produto["Estoque"] = produto["Estoque"] - 2
produto.pop["Marca"]

produto

#Notas

notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}

print("Notas dos alunos:")
for aluno, nota in notas.items():
    print(f"{aluno}: {nota}")
media = sum(notas.values()) / len(notas)
print(f"A média é: {media}")

notas.keys()
notas.values()



# Soma de Valores
# Dado um dicionário com valores numéricos, percorra o dicionário e some todos os valores.
# Exemplo:
# numeros = {"a": 10, "b": 20, "c": 30}
# Saída esperada: 60

numeros = {
    "a": 10,
    "b": 20,
    "c": 30
}

soma = sum(numeros.values())
print(soma)

# Contagem de Itens Repetidos
# Dado uma lista de elementos, conte a frequência de cada elemento utilizando um dicionário.
# Exemplo:
# lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
# Saída esperada: {'maçã': 3, 'banana': 2, 'laranja': 1}

lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = {}

for item in lista:
    if item in frequencia:
        frequencia[item] += 1
    else:
        frequencia[item] = 1
print(frequencia)

# Filtrando Dicionário
# Dado um dicionário contendo produtos e seus preços, filtre os produtos que custam mais de R$ 50,00.
# Exemplo:
# produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
# Saída esperada: {"mochila": 80, "notebook": 3000}

produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}

filtro = {}
for item, custo in produtos.items():
    if custo >= 50:
        filtro[item] = custo
print(filtro)

# Tradutor Simples
# Crie um dicionário chamado 'tradutor' que contém algumas palavras em inglês como chaves e suas traduções para português como valores.
# Peça ao usuário para digitar uma palavra em inglês e exiba sua tradução, caso exista no dicionário.
# Se a palavra não estiver cadastrada, exiba "Palavra não encontrada".

tradutor = {
    "Key": "Chave",
    "Value": "Valor",
    "Term": "Termo",
    "Dictionary": "Dicionário"
}

palavra = input("Digite uma palavra em inglês: ")
if palavra in tradutor:
    print(f"Tradução: {tradutor[palavra]}")
else:
    print("Palavra não encontrada.")

# Lista de Compras
# Crie um dicionário onde as chaves são nomes de produtos e os valores são quantidades.
# Permita ao usuário adicionar produtos, atualizar quantidades e remover itens.
# No final, exiba a lista completa de compras.

compras = {}

nome = str(input("Digite o que pretende adicionar na lista: "))
compras[nome]

# Inicializa o dicionário da lista de compras
lista_compras = {}

while True:
    print("\n--- Menu da Lista de Compras ---")
    print("1. Adicionar produto")
    print("2. Atualizar quantidade")
    print("3. Remover produto")
    print("4. Exibir lista")
    print("5. Sair")

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == "1":
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        lista_compras[produto] = quantidade
        print(f"{produto} adicionado com quantidade {quantidade}.")

    elif escolha == "2":
        produto = input("Produto a atualizar: ")
        if produto in lista_compras:
            nova_quantidade = int(input("Nova quantidade: "))
            lista_compras[produto] = nova_quantidade
            print(f"Quantidade de {produto} atualizada para {nova_quantidade}.")
        else:
            print(f"{produto} não está na lista.")

    elif escolha == "3":
        produto = input("Produto a remover: ")
        if produto in lista_compras:
            del lista_compras[produto]
            print(f"{produto} removido da lista.")
        else:
            print(f"{produto} não está na lista.")

    elif escolha == "4":
        print("\n--- Lista de Compras ---")
        if lista_compras:
            for produto, quantidade in lista_compras.items():
                print(f"{produto}: {quantidade}")
        else:
            print("A lista está vazia.")

    elif escolha == "5":
        print("\nEncerrando... Lista final:")
        for produto, quantidade in lista_compras.items():
            print(f"{produto}: {quantidade}")
        break

    else:
        print("Opção inválida. Tente novamente.")

