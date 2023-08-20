def count_substring(string, sub_string):
    count = 0
    sub_length = len(sub_string)

    for i in range(len(string) - sub_length + 1):
        if string[i : i + sub_length] == sub_string:
            count = count + 1

    return count


if __name__ == "__main__":
    stringFirst = input().strip()
    sub_string = input().strip()

    count = count_sub_string(stringFirst, sub_string)
    print(count)
