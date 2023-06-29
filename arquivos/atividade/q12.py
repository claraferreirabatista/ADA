#Crie uma lista com 10 números quaisquer:


array_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a. uma lista com os 4 primeiros números

a = array_number[:4]

# b. uma lista com os 5 últimos números
b = array_number[5:]

# c. uma lista contendo apenas os elementos das posições pares
c = array_number[1::2]

# d. uma lista contendo apenas os elementos das posições ímpares
d = array_number[0::2]

# e. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista sorteada e termina com o primeiro)
e = array_number[::-1]

# f. uma lista inversa dos 5 primeiros números
f = array_number[4::-1]

# g. uma lista inversa dos 5 últimos números.
g = array_number[:5][::-1]



"""# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a. A list with the first 4 numbers
first_four = []
for i in range(4):
    first_four.append(numbers[i])

# b. A list with the last 5 numbers
last_five = []
for i in range(len(numbers) - 5, len(numbers)):
    last_five.append(numbers[i])

# c. A list containing only the elements at even positions
even_positions = []
for i in range(1, len(numbers), 2):
    even_positions.append(numbers[i])

# d. A list containing only the elements at odd positions
odd_positions = []
for i in range(0, len(numbers), 2):
    odd_positions.append(numbers[i])

# e. The reversed list of the original list
reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

# f. A reversed list of the first 5 numbers
reversed_first_five = []
for i in range(4, -1, -1):
    reversed_first_five.append(numbers[i])

# g. A reversed list of the last 5 numbers
reversed_last_five = []
for i in range(len(numbers) - 1, len(numbers) - 6, -1):
    reversed_last_five.append(numbers[i])

# Printing the lists
print("a. First four numbers:", first_four)
print("b. Last five numbers:", last_five)
print("c. Elements at even positions:", even_positions)
print("d. Elements at odd positions:", odd_positions)
print("e. Reversed list:", reversed_list)
print("f. Reversed first five numbers:", reversed_first_five)
print("g. Reversed last five numbers:", reversed_last_five)"""







