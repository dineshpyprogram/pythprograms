import os
import random
import string
#i = 0
count = 1
file_dir = "/home/dinesh/PycharmProjects/random/"

while count <= 10:
    file_name = "random_{}.txt".format(count)
    i = 0
    while i < 104857601:
        with open("{}{}".format(file_dir, file_name), "a") as file:
            ran_str = ''.join([random.choice(string.ascii_letters+string.digits) for n in range(512)])
            file.write("%s" % ran_str)
            i = os.path.getsize("{}{}".format(file_dir, file_name))
    count = count+1
print(count)
