import os
import random
import string
import datetime
from datetime import date, time
count = 1
file_dir = "/home/dinesh/PycharmProjects/random/"

while count <= 10:
    date_file = datetime.datetime.now().strftime("%d_%m_%y_%H_%M_%S")
    file_name = "file_{}".format(date_file)
    i = 0
    while i < 104857601:
        with open("{}{}".format(file_dir, file_name), "a") as file:
            ran_str = ''.join([random.choice(string.ascii_letters+string.digits) for n in range(512)])
            file.write("%s" % ran_str)
            i = os.path.getsize("{}{}".format(file_dir, file_name))
    count = count+1
print(count)
