from itertools import product

firstArray = list(map(int, input().split()))
secondArray = list(map(int, input().split()))
cartesionProduct = list(product(firstArray, secondArray))

for pair in cartesionProduct:
    print(pair, end=" ")
