lista = []
nome = "Gabriel"
idade = 19
email = "123@gmail.com"
lista = [nome, idade, email]
lista[-2]


#frutas
frutas = ["Banana", "Maçã", "Laranja", "Uva"]

#elemento

frutas[0]
frutas[-1]

#manga

frutas.append("Manga")
 
#remover banana
frutas.remove("Banana")

#substituir laranja

indice = frutas.index("Laranja")
frutas[indice] = "Abacaxi"

#números 1 a 10

numeros = list(range(1,11))
numeros

#soma dos números

soma = sum(numeros)

print(soma)

#encontre o maior e menor da lista

max(numeros)
min(numeros)

#números invertidos
list(reversed(numeros))

#cidades
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
cidades

#ordem alfabética

sorted(cidades)

#adicionar Porto Alegre

cidades.append("Porto Alegre")

#Número de Curitiba

indice = cidades.index("Curitiba")

#listas de números

lista1 = list(range(1,4))
lista2 = list(range(4,7))

#junção das listas

lista3 = lista1 + lista2

#Imprimir lista 3

print(lista3)

#animais

animais_domesticos = ["cachorro", "gato", "coelho"]
animais_selvagens = ["leão", "tigre", "urso"]

#junção

todos_animais = animais_domesticos + animais_selvagens

#imprimir nova lista

print(todos_animais)

#nomes

nomes = ["Ana", "Pedro", "Maria", "João"]

for i in nomes:
    print(nomes)

nomes_maiusculo = ["ANA", "PEDRO", "MARIA", "JOÃO"]

for i in nomes_maiusculo:
    print(nomes_maiusculo)

#numeros

numeros3 = list(range(1,21))
for pares in numeros3:
   if pares % 2 == 0:
       print(pares)

for quadrado in numeros3:
    aoquadrado = quadrado * quadrado
    print(f"{aoquadrado}")

#linguagens

palavras = ["python", "java", "c", "javascript"]

for palavra in palavras:
    tamanho = len(palavra)
    print(f"A palavra {palavra} tem {tamanho} letras.")

#idades

idades = [12, 18, 25, 40, 60]

for idade in idades:
    menor = idade < 18
    maior = idade >= 18
    if maior:
        print(f"Maior de idade: {idade}")
    else:
        print(f"Menor de idade: {idade}")

#temperaturas

temperaturas = [10, 20, 30, 40, 50, 60, 70]
for temp in temperaturas:
    if temp > 30:
        print("Dia quente")
    else:
        print("Dia agradável")

#notas

decimais = [5.5, 7.0, 8.3, 4.9, 6.2]
aprovados = 0
reprovados = 0
   
for notas in decimais:
    if notas >= 7:
        aprovados += 1
    elif notas < 7:
        reprovados += 1

print(f"{aprovados} pessoas foram aproadas.")
print(f"{reprovados} pessoas foram reprovadas.")

#Palindromos

palindromo = ["arara", "banana", "radar", "python"]

for palindromos in palindromo:
    if palindromos == palindromos[::-1]:
        print(f"A palavra {palindromos} é um palíndromo")

#Compras

compras = ["arroz", "feijão", "batata", "carne"]

for necessario in compras:
    print(f"Preciso comprar {necessario}")

#1 a 10 com while

numero = 1
while numero <=10:
    print(numero)
    numero = numero + 1

#Número do usuário

while True:
    numero = int(input("Digite seu número:"))
    print(numero)
    if numero == 0:
        print("Número 0 digitado.")
        break

#Soma 1 a 100

numero = 1
soma = 0
while numero <= 100:
    soma = soma + numero
    numero += 1
    print(soma)

#Número secreto

while True:
    numero = int(input("Digite um número:"))
    print(numero)
    if numero == 16:
        print("Número correto")
        break

#Pares

numero = 2

while numero <= 20:
    print(numero)
    numero += 2

#Ímpares

numero = 1

while numero <= 20:
    print(numero)
    numero += 2

