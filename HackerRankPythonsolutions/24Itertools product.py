from itertools import product

first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))
cartesian_product = list(product(first_array, second_array))

for pair in cartesian_product:
    print(pair, end=" ")
