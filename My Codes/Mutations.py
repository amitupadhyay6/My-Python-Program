
def mutate_string(string, position, character):
    c = ""
    i=0
    for i in range(len(string)):
        if i == position:
            c = c + character
            i += 1
        else:
            c = c + string[i]
            i += 1
    return c


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
