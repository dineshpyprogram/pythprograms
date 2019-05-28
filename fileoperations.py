# Reading a file that has string names in it
file = open('/home/dinesh/duplicates_file', 'r')
t = file.readlines()
l = []

for x in t:
    print(x)
    if x.strip() not in l:
        l.append(x.strip())

print("Printing the file without duplicates \n")
print([l])

print("Now writing the list of names into a file \n")

with open('/home/dinesh/PycharmProjects/output.txt', 'w') as file:
    for data in l:
        file.writelines("%s " % data)

with open('/home/dinesh/PycharmProjects/output.txt', 'r') as f:
    n = f.readlines()
    print([n])







