stamp_collection = []
s = set()
for i in range(int(input())):
    stamp_collection.append(input())

for i in stamp_collection:
    s.add(i)
print(len(s))

