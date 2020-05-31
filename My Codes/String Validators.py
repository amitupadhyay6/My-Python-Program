#In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
#In the second line, print True if  has any alphabetical characters. Otherwise, print False.
#In the third line, print True if  has any digits. Otherwise, print False.
#In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
#In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

s = input()
x = y = z = k = l = "False"
for item in s:
    if item.isalnum():
        x = item.isalnum()
    if item.isalpha():
        y = item.isalpha()
    if item.isdigit():
        z = item.isdigit()
    if item.islower():
        l = item.islower()
    if item.isupper():
        k = item.isupper()
print(x)
print(y)
print(z)
print(l)
print(k)


