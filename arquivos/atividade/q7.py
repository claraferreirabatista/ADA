"""Faça um programa que imprima o maior número de uma lista, sem usar o método max()."""


number_list = [10, 5, 8, 15, 3, 20, 7]
largest_number = number_list[0]

for number in number_list:
    if number > largest_number:
        largest_number = number

print("The largest number in the list is:", largest_number)

