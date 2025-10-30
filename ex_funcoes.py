# 1. Crie uma função lambda que calcule f(x) = x². Teste com x = 4.

f = lambda x: x**2
resultado = f(4)
print(resultado)

# 2. Crie uma função lambda que calcule f(x) = 5x - 3. Teste com x = 2.

f = lambda x: 5*x - 3
resultado = f(2)
print(resultado)

# 3. Crie uma função lambda que calcule f(x) = x² + 2x + 1. Teste com x = -1, 0, 1.

f = lambda x: x**2 - 2*x
resultado = f(2)
print(resultado)

# 4. Crie uma função lambda que calcule f(x, y) = x^2 + 2xy + y^2. Teste com x = 2, y= 4.

f = lambda x, y: x**2 + 2*x*y + y**2
resultado = f(2, 4)
print(resultado)

# 5. Crie uma função lambda que calcule f(x, y, z) = x^y+z. Teste com x = 3, y = 2, z=10.

f = lambda x, y, z: x**(y+z) 
resultado = f(3, 2, 10)
print(resultado)

# 6. Escreva uma função def lucro(receita, custo) que retorne o lucro da empresa:
# Lucro = Receita - Custo. Teste com receita = 10.000 e custo = 7.500.

def lucro(receita, custo):
    lucro = receita - custo
    return lucro
receita = 10000
custo = 7500
lucro(receita, custo)

# 7. Escreva uma função def margem_lucro(receita, custo) que calcule a margem de lucro percentual:
# Margem = (Lucro/Receita) * 100. Teste com receita = 20.000 e custo = 15.000.

def margem_lucro(receita, custo):
    lucro = receita - custo
    margem = (lucro / receita) * 100
    return margem
receita = 20000
custo = 15000

margem_lucro(receita, custo)

# 8. Escreva uma função def ponto_equilibrio(custo_fixo, preco, custo_variavel) que calcule a quantidade mínima a ser vendida para não ter prejuízo:
# Qe = Custo Fixo / (Preço - Custo Variável). Teste com CF = 5.000, preço = 50, custo variável = 30.

def ponto_equilibrio(custo_fixo, preco, custo_variavel):
    Qe = custo_fixo / (preco - custo_variavel)
    return Qe
custo_fixo = 5000
preco = 50
custo_variavel = 30

ponto_equilibrio(custo_fixo, preco, custo_variavel)

# 9. Escreva uma função def folha(funcionarios) que receba uma lista de dicionários com nome e salário e retorne o total da folha salarial:
# [{'nome': 'Ana', 'salario': 3000}, {'nome': 'Carlos', 'salario': 4500}].

def folha(funcionarios):
    total = 0
    for funcionario in funcionarios:
        total = total + funcionario["salario"]
    return total

lista = [{'nome': 'Ana', 'salario': 3000}, {'nome': 'Carlos', 'salario': 4500}]

total = folha(lista)
print(total)

# 10. Escreva uma função def juros_compostos(capital, taxa, tempo) que calcule o montante:
# M = C * (1+i)^t. Teste com C = 1.000, i = 0.02, t = 12.

def juros_compostos(capital, taxa, tempo):
    M = capital * (1+taxa)**tempo
    return M
capital = 1000
taxa = 0.02
tempo = 12

montante = juros_compostos(capital, taxa, tempo)
print(f"{montante: .2f}")