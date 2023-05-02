# python list comprehensions problem
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # remove all the arrays that do not fall under the summation condition
    list_comp = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n]
    print(list_comp)

    
# the item and iterable variables should be different in the above case for list comprehensions logic to work