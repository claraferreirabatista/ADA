"""Faça um programa que dadas duas listas de mesmo tamanho, imprima o produto escalar entre elas.
"""

"""list1 = [2, 4, 6]
list2 = [1, 3, 5]
if len(list1) != len(list2):
    print("Error: As lista devem ter o mesmo tamanho!!")
else:
    dot_product = 0
    for i in range(len(list1)):
        dot_product += list1[i] * list2[i]

    print("Resultado:", dot_product)"""


"""def dot_product(list1, list2):
    if len(list1) != len(list2):
        return None

    result = 0
    for i in range(len(list1)):
        result += list1[i] * list2[i]

    return result"""


list1 = [1, 2, 3]
list2 = [4, 5, 6]

product = dot_product(list1, list2)
if product is not None:
    print("Resultado", product)
else:
    print("Error: As lista devem ter o mesmo tamanho!!")
