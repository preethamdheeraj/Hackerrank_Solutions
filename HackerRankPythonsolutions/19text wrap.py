import textwrap


def wrap(string, max_width):
    wrappedString = ""
    for i in range(0, len(string), max_width):
        wrappedString = wrappedString + string[i : i + max_width] + "\n"
    return wrappedString


if __name__ == "__main__":
    string, maxWidth = input(), int(input())
    result = wrap(string, maxWidth)
    print(result)
