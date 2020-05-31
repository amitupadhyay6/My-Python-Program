
def print_formatted(number):
    i = 1
    x=(len(bin(number)) - 2)*""
    while i <= number:
        print(i,x,oct(i).upper()[2:],x,hex(i).upper()[2:],x,bin(i)[2:])
        i += 1


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


######################### New Method ############################

#n = int(input())
#width = len("{0:b}".format(n))
#print(width)
#for i in range(1,n+1):
 # print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
