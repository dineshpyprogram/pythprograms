#   ############### This is a python program to print a person's profile page into a file ######################

first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
birth_month = input("Enter the month in which you were born: ")
birth_day = input("Enter the day of the month you were born: ")
birth_year = input("Enter the year in which you were born: ")
gender = input("Enter your Gender: ")
password = input("Enter a password: ")
email = input("Enter your Email: ")

name = "{} {} {}".format("Name:".ljust(30, " "), first_name.capitalize(), last_name.capitalize())
birthday = "%s %s, %s %s" % ("Birthday:".ljust(30, " "), birth_month.capitalize(), birth_day, birth_year)
gender = "%s %s" % ("Gender:".ljust(30, " "), gender.capitalize())
password = "%s %s" % ("Password:".ljust(30, " "), password)
email = "%s %s" % ("Email:".ljust(30, " "), email)

l = [name, birthday, gender, password, email]


with open('/home/dinesh/biodata.txt', 'w') as f:
    for i in l:
        f.write(i)
        f.write("\n")
