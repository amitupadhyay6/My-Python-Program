
n = int(input())
eng_roll = list(map(int, input().strip().split()[:n]))
b = int(input())
fren_roll = list(map(int, input().strip().split()[:b]))

stu_opt = set(eng_roll)
stu_opt = stu_opt.union(fren_roll)
print(len(stu_opt))
