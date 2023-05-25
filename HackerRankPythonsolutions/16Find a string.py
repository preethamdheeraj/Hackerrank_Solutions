def count_substring(string, subString):
    count = 0
    subLength = len(subString)

    for i in range(len(string) - subLength + 1):
        if string[i : i + subLength] == subString:
            count = count + 1

    return count


if __name__ == "__main__":
    stringFirst = input().strip()
    sub_string = input().strip()

    count = count_substring(stringFirst, sub_string)
    print(count)
