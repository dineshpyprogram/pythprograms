#   ############### This is a python program to print a person's profile page ######################

first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
birth_month = input("Enter the month in which you were born: ")
birth_day = input("Enter the day of the month you were born: ")
birth_year = input("Enter the year in which you were born: ")
gender = input("Enter your Gender: ")
password = input("Enter a password: ")
email = input("Enter your Email: ")


# ##############Printing the output####################################################
print("\n\n\n\nProfile\n")
print("Some info may be visible to other people using Google services. Learn more\n\n\n")
print("Your name is: ".ljust(30, " "), "{} {}\n".format(first_name.capitalize().ljust(0, " "), last_name.capitalize()))
print("Your birthday is: ".ljust(30, " "), "%s %s, %s\n" % (birth_month.capitalize().ljust(0, " "), birth_day, birth_year))
print("Your gender is: ".ljust(30, " "), "%s\n" % (gender.capitalize().ljust(0, " ")))
print("Your password is: ".ljust(30, " "), "{}\n\n\n".format(password.ljust(0, " ")))
print("Contact info\n")
print("Your email is: ".ljust(30, " "), "{}".format(email.ljust(0, " ")))
