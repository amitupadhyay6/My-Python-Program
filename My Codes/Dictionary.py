# we associate keys (name) with values (details). Note that the key must be unique just like you cannot find out the correct information if you
# have two persons with the exact same name.Note that you can use only immutable objects (like strings) for the keys of a dictionary but
# you can use either immutable or mutable objects for the values of the dictionary.
'''Pairs of keys and values are specified in a dictionary by using the notation d = {key1 :
value1, key2 : value2 } . Notice that the key-value pairs are separated by a colon and the
pairs are separated themselves by commas and all this is enclosed in a pair of curly braces.'''

ab= {"Amit" : "amitupadhyay6@gmail.com", "Vibha":"vibha190890@gmail.com","Eva":"avni180617@gmail.com", "Spam":"spam@gmail.com"}

print("Eva's email address is", ab["Eva"])
print("Full dictionary is ", ab)
# Delete the spam from the list
del ab["Spam"]
print("After deleting the spam from the list, the list is", ab)

for name, address in ab.items():
    print("Contact {} at {}".format(name,address))
#Adding new pair in the exiting list
ab["Emmy"]="amit_246453@yahoo.co.in"
for nam, add in ab.items():
    print("Updates list are : contact {} at {}".format(nam,add))





