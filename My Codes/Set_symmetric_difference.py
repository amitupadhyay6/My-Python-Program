
n = int(input())
eng_news = list(map(int, input().strip().split()[:n]))
m = int(input())
fren_news = list(map(int, input().strip().split()[:m]))

s_sym_diff = set(eng_news)
s_sym_diff = s_sym_diff.symmetric_difference(fren_news)
print(len(s_sym_diff))

