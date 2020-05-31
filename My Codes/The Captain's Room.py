
sizeofgroup = int(input())
room_number_list = list(map(int, input().strip().split()))
unique_room_num = set(room_number_list)

for item in unique_room_num:
    room_number_list.remove(item)
room_without_cap = set(room_number_list)
caption_room = unique_room_num.difference(room_without_cap)

for item in caption_room:
    print(item)


