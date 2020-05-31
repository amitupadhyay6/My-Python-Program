n = int(input())
eng_new = list(map(int, input().strip().split()[:n]))
b = int(input())
fren_new = list(map(int, input().strip().split()[:b]))

intersect_news = set(eng_new)
intersect_news = intersect_news.intersection(fren_new)
print(len(intersect_news))
