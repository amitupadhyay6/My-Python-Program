import re

for _ in range(int(input())):
    print(bool(re.match(r'^[+-]?[0-9]*\.[0-9]+$', input())))


# r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|net|edu)'
# start with (a-z or A-Z or 0-9 or . or -) and + shows, one or more time till @
# @ (a-z or A-Z or 0-9 or -) and + shows, one or more time till .
# . (com|net|edu) either one of the group
# Total number of group is 2 here one is whole group, 2nd one is (com|net|edu)
#
#
#
# r'^[+-]?[0-9]*\.[0-9]+$'
# ^ it says start with (+ or -) ? says zero or one time then (0-9) * says zero or more time till .
# . (0-9) + says 1 or more times and $ end here

