name = input("\nName (first name and last name): ")

firstName, lastName = name.split()

username = (firstName[0] + lastName[:7]).lower()

print("Username: {}".format(username))
