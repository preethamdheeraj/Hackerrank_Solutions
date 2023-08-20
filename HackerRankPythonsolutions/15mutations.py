def mutate_string(string, position, character):
    list_number_one = list(string)
    list_number_one[position] = character
    stringReturn = "".join(list_number_one)
    return stringReturn


if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
