# finding the second largest number in an array using min and max functions in python3
def secondLargest(array):
    if len(array) < 2:
        return None

    largest = max(array[0], array[1])
    second_largest = min(array[0], array[1])
    for i in range(2, len(array)):
        if array[i] > largest:
            second_largest = largest
            largest = array[i]
        elif array[i] > second_largest and array[i] < largest:
            second_largest = array[i]

    return largest, second_largest


array = [5, 8, 2, 10, 15, 3, 7]
largest, second_largest = secondLargest(array)
print(
    "the first largest is {} followed by the second largest {}".format(
        largest, second_largest
    )
)
