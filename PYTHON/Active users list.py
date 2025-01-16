# active_users contains currently used email addresses

active_users = ["OAmaro@company.com" , "JGonzalez@company.com" , "MCerqueira@company.com"]

# first_name variable contains the user's first name
# last_name variable contains the user's last name
# desired email format is first initial + last name + @company.com

first_name_request = input("Please enter the user's first name: ")
# print(first_name_request)

last_name_request = input("Please enter the user's last name: ")
# print(last_name_request)

first_name = first_name_request
last_name = last_name_request


# new_user variable combines previous first_name and last_name var into single var

new_user = ((first_name[0]) + last_name + "@company.com")

# if statement checks if new_user is already in active_users 
# else new_user is appended to active_users and success msg is returned

if new_user in active_users:
    print("Username not available")
else:
    active_users.append(new_user)
    print("Username available")

print(active_users)