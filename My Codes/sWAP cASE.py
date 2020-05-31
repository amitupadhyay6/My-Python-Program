def swap_case(st):
    cd = ""
    i = 0
    while i <len(st):
        if st[i].isalpha():
            if st[i].isupper() == True:
                cd=cd + (st[i].lower())
                i += 1
            else:
                cd=cd + (st[i].upper())
                i += 1
        else:
            cd=cd + (st[i].lower())
            i += 1
    return cd

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
