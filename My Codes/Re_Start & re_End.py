import re

str = input()
kst=input()
kst = re.compile(kst)

mat = kst.search(str)
# mak = re.finditer(kst, str)
# print([(i.start(), i.end()) if mak else (-1, -1) for i in mak])

if not mat: print((-1, -1))
while mat:
    print("({0}, {1})".format(mat.start(), mat.end() - 1))
    mat = kst.search(str,mat.start() + 1)




    #print(mat.start(),mat.end())
