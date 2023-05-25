def gernerateDoorMat(rows, columns):
    pattern = ".|."
    welcomeMessage = "WELCOME"

    for i in range(rows // 2):
        row = (pattern * (2 * i + 1)).center(columns, "-")
        print(row)
    welcomeRow = welcomeMessage.center(columns, "-")
    print(welcomeRow)

    for i in range(rows // 2 - 1, -1, -1):
        row = (pattern * (2 * i + 1)).center(columns, "-")
        print(row)


if __name__ == "__main__":
    n, m = map(int, input().split())
    gernerateDoorMat(n, m)
