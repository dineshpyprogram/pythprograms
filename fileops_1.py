import os
import datetime
from datetime import date, time
import random
import string
import fnmatch
count = 1
file_dir = os.getcwd()
print(file_dir)
n = len(fnmatch.filter(os.listdir(file_dir), "file_*_*_*"))



while count <= 10:
    date_file = datetime.datetime.now().strftime("%d_%m_%y_%H_%M_%S")
    file_name = "file_{}".format(date_file)
    i = 0
    while i < 104857601:
        with open("{}/{}".format(file_dir, file_name), "a") as file:
            ran_str = ''.join([random.choice(string.ascii_letters+string.digits) for n in range(512)])
            file.write("%s" % ran_str)
            i = os.path.getsize("{}/{}".format(file_dir, file_name))
    print(str(n+count).ljust(10, " "), date_file.ljust(10, " "), file_name.ljust(10, " "))
    count = count+1

