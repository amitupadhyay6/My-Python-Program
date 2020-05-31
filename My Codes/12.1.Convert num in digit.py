
dic={
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"Six",
    0:"Zero"
}
cd=input("Enter your 4 digit mobile num = ")

print(dic.get(int(cd[0])),dic.get(int(cd[1])),dic.get(int(cd[2])),dic.get(int(cd[3])))

## or keys can be defined as string like "2".

cd=input("> ")
ab=cd.split()
print(ab)
