import time

start = time.time()
cube = lambda x: pow(x,3)

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        fibnocci_list = [0,1]
        i = 2
        while i < n:
            fibnocci_list.append(fibnocci_list[i-1]+ fibnocci_list[i-2])
            i +=1
        return fibnocci_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    print((time.time()- start)*1000)

