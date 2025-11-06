#par ou ímpar
#leia um número inteiro e informe se ele é par ou é ímpar
num1=int(input("Digite seu número: "))

if num1 % 2 == 0:
    print("É par")
else:
    print("É ímpar")

#aprovado ou reprovado


ap1 =float(input("Digite sua nota da AP1: "))
ap2 =float(input("Digite sua nota da AP2: "))
ac=float(input("Digite sua nota da AC: "))
media = 0.4 * ap1 + 0.4 * ap2 + 0.2 * ac

if media >= 7:
    print((f"Sua nota é: {media}. Você passou."))
else:   
    print((f"Sua nota é: {media}. Você reprovou."))

#cálculo de desconto

valor = float(input("Digite o valor da sua compra: "))
if valor > 100:
    preco = valor - valor * 0.1
    print(f"Desconto de 10% aplicado à sua compra, totalizando: {preco}")
else:
    print(f"Valor final é: {valor}")

#Conversão de temperatura

temp1 = float(input("Digite a temperatura em Celsius"))
temp2 = float(temp1 * 9) / 5 + 32
print((f"A temperatura em fahrenheit é igual à: {temp2}"))

#maior número 2 valores

num1 = float(input("Digite seu número: "))
num2 = float(input("Digite seu segundo número: "))
if num1 > num2:
    print((f"O número {num1} é maior que o {num2}"))
elif num1 == num2:
    print((f"O número {num1} é igual ao {num2}"))
else:
    print((f"O número {num2} é maior que o {num1}"))

#maior número 3 valores

num11 = float(input("Digite seu número: "))
num12 = float(input("Digite seu segundo número: "))
num13 = float(input("Digite seu terceiro número: "))
maior = num11
if maior < num12:
    maior = num12
if maior < num13:
    maior = num13
print((f"O maior número é o {maior}"))

#calculadora

n1 = int(input("Digite um número: "))
n2 = int(input("Digite o segundo número: "))
calc = (input("Digite a operação desejada (+, -, / ou *): "))
adc = n1 + n2
mns = n1 - n2
vzs = n1 * n2
dvs = n1 // n2
if calc=="+":
    print((f"A resposta é {adc}"))
elif calc=="-":
    print((f"A resposta é {mns}"))
elif calc=="*":
    print((f"A resposta é {vzs}"))
elif calc=="/":
    if n2!=0:
     print((f"A resposta é {dvs}"))
    else:
        print((f"Operação inválida."))
