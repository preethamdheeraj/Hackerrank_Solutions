if __name__ == '__main__':
    N = int(input())   # this will specify the number of commands
    # the elements added to the list must be integers
    listOne = []

    for i in range(0, N):
        command = input().split()
        if command[0] == "insert":
            listOne.insert(int(command[1]), int(command[2]))
        elif command[0] == "append":
            listOne.append(int(command[1]))
        elif command[0] == "pop":
            listOne.pop()
        elif command[0] == "print":
            print(listOne)
        elif command[0] == "remove":
            listOne.remove(int(command[1]))
        elif command[0] == "sort":
            listOne.sort()
        else:
            listOne.reverse()
