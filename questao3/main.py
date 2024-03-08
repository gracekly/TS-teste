import json

with open('dados.json', 'r') as f:
    data = json.load(f)

valores = []

for d in data:
    valor = d['valor']
    valores.append(valor)

print(valores)

maior_valor = valores[0]
menor_valor = valores[0]
cont = 0
soma = 0
media = 0

for valor in valores:
  if valor > maior_valor:
    maior_valor = valor

  if valor < menor_valor:
    menor_valor = valor

  cont += 1
  soma += valor

media = soma/cont


print(f'\nmenor valor: {menor_valor}')
print(f'maior valor: {maior_valor}')

print(f'\ndias: {cont}')
print('media mensal: {:4f}'.format(media))

cont = 0
for valor in valores:
  if valor > (media):
    cont +=1

print(f'\nnúmero de dias no mês em que o valor de faturamento foi superior à média mensal: {cont}')