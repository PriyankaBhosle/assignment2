# create the dict whose alphabet from a-z

dict = {}

for i in range (97, 97 + 26):
    dict[chr(i)] = i
    i = i + 1
print(dict) 

# create the dict whose alphabet start from A to Z

my_dict = {}

for i in range (65, 65 + 26):
    my_dict [chr(i)] = i
print(my_dict)