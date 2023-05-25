# complete the solve function below

import os


def solve(string):
    return " ".join([i.capitalize() for i in string.split(" ")])


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    string = input()
    result = solve()
    fptr.write(result + "\n")
    fptr.close()
