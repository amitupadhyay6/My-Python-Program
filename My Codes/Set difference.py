
n = int(input())
eng_news = list(map(int, input().strip().split()[:n]))
m = int(input())
fren_news = list(map(int, input().strip().split()[:m]))

sdiff = set(eng_news)
sdiff = sdiff.difference(fren_news)
print(len(sdiff))
