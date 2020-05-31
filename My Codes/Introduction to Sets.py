def average(array):
    array = set(array)
    x = 0
    for item in array:
        x = x + item
    return x/len(array)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
