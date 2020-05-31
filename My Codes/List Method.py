a=[0,4,3,2,1,2]
b=["c","b","a"]
a.sort() #Sort function to sort the list.
b.sort()
print(a , b)
print(a.sort()) # New list is not returned. hence we need to store the info in another object.
a.append(5)
print("Append the list with the item \"5\"", a)
a.append(("a", "b"))
print("Append the list with new list", a)
a.extend(b)
print("Extend the list with another existing list", a)
print("Index of \"5\"", a.index(5))
a.insert(6,"SIX")
print("Intem insterted @index 6 is ", a[6])
a.pop()
print("without parameter pop removes the last item in the list", a)
print("Print the occurrences of number 2 in the list", a.count(2))
print("Length of the list",len(a))
a.pop(8)
print("Length of the list after index 8 item has been removed and the list",len(a), a)
a.remove(2)
print("number 2 has been removed from the list", a)
a.reverse()
print("Reverse the list or opposite of the sort function", a)

