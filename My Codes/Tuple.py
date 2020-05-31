# One major feature of tuples is that they are immutable/(will not change) like strings i.e. you cannot modify tuples.
# Tuples are defined by specifying items separated by commas within an optional pair of parentheses.

# parentheses are best option but in this case these are optional
zoo="cat","mouse","rat"
print("numbers of animal in the zoo are ",len(zoo), " and animals in zoo are ", zoo)
# without parentheses, but i should use parentheses for better indentation.
nzoo=("Lion","Tiger","Gorilla",zoo)
print("\n")
print("Number of animal in new zoo are ,",len(nzoo), " and animals in the new zoo are ", nzoo)
print("Animals bought from old zoo are", nzoo[3])
print("Total number of animal in new Zoo are ", len(nzoo)+len(nzoo[3])-1)

# To check last tuple using the new tuple use[] twice
print("\nLast animal bought from the old zoo was ", nzoo[3][2])



