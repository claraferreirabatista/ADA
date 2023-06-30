"""Faça um programa que olhe todos os itens de uma lista e diga quantos deles são par."""

list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0

for i in list_number:
    if i % 2 == 0:
        count += 1

print("O total de números pares na lista é:", count)

"""num = int(input('Digite um número: '))


i = 0
lista = []
for i in range(num):
    lista.append(i)
    i += 1
print(lista)"""





