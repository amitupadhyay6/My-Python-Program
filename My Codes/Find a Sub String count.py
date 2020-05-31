
def count_substring(str, sub_string):
    i = 0
    count = 0
    n = len(sub_string)
    for i in range(len(str)):
        if str[i:i+n] == sub_string:
            count += 1
            i += 1
        else:
            i += 1
    return count
#BlUeBe1Bl*fjal9jkl
str = input().strip()
sub_string = input().strip()

count = count_substring(str, sub_string)
print(count)
