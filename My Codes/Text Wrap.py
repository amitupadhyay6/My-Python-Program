
def wrap(string, max_width):
    i=0
    d=""
    while i < len(string):
        if (i + max_width) < len(string):
            d = d + string[i:i+max_width] + "\n"
            i += max_width
        else:
            d = d + string[i:]
            break
    return d

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
