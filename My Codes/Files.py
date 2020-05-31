
input=open("Amit.txt")
for line in input.readlines():
    print(line)
input.close()

print("open .py file")
ab=open("Tuples.py")
for i in ab.readline():
    print(i)
ab.close()

