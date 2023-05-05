# print("this is runnning")
# print('G', 'F', sep='', end='')
# print('G')
# # \n provides new line after printing the year
# print('09', '12', '2016', sep='-', end='\n')

# print('prtk', 'agarwal', sep='', end='@')
# print('geeksforgeeks')


# '''
# i = 5
# while True:
#     if i % 0o11 == 0: here 0o11 is 9 in base 10 style of numbering
#         break
#     print(i)
#     i += 1
# '''


# i = 5
# while True:
#     if i % 0o11 == 0:
#         break
#     print(i)
#     i += 1


# i = 2
# while True:
#     if i % 3 == 0:
#         break
#     print(i)
#     i += 2

# x = 2021
# for i in x:
#   print(i)  Objects of type int are not iterable instead a list, dictionary or a tuple should be used.

# matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# matrix2 = []

# for submatrix in matrix:
#     for val in submatrix:
#         matrix2.append(val)

# print(matrix2[0])
# the output of this solutions will be 0

# a = []
# for i in range(2):
#     a.append([])  #  this will add two empty sublists to the main list
#     for j in range(2):
#         a[i].append(j)

# print(a)


a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)  # this will print 5 * 6
print(a[2][3])
