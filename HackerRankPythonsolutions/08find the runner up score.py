# to find the runner up score
if __name__ == "__main__":
    n = int(input())  #  this is the length of size of the array
    arr = map(
        int, input().split()
    )  #  using sort to get the 2nd last item as 2nd largest
    listOne = list(set(arr))
    listOne.sort()
    print(listOne[-2])
