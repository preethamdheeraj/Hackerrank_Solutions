if __name__ == "__main__":
    N = int(input())  # this will specify the number of commands
    # the elements added to the list must be integers
    list_one = []

    for i in range(0, N):
        command = input().split()
        if command[0] == "insert":
            list_one.insert(int(command[1]), int(command[2]))
        elif command[0] == "append":
            list_one.append(int(command[1]))
        elif command[0] == "pop":
            list_one.pop()
        elif command[0] == "print":
            print(list_one)
        elif command[0] == "remove":
            list_one.remove(int(command[1]))
        elif command[0] == "sort":
            list_one.sort()
        else:
            list_one.reverse()
