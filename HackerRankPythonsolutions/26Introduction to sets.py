def average(array):
    # your code goes here
    arr = int(input())
    roundedValue = round(arr, 3)
    return roundedValue


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    result = average(array)
    print(result)
