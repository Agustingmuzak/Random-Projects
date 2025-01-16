#The objective of this project is to create and manage two lists using indexes
#The lists will contain a user's email, name and age and synchronize them by index
#If successful we will be able to retrieve all three data points by just entering one of them

#-------------------------------------------------------------------------------------------------------#

def input_request1(name,email,age):
    email_list.append(email)
    name_list.append(name) 
    age_list.append(age)
    print("The user was added successfully with the following details:\nName: ", name, " | ", "Email: ", email, " | ", "Age: ", age, " |",)

def input_request2(email):
    if email in email_list:
       indexresult = email_list.index(email)
       print("User name: ", name_list[indexresult], " | Email: ", email_list[indexresult], " | Age: ", age_list[indexresult]," |")
    else: 
        print("User not available")

#-------------------------------------------------------------------------------------------------------#

email_list = ["agustin.gonzalez@company.com", "micaela.cerqueira@company.com", "olga.amaro@company.com"]
name_list = ["Agustin Gonzalez", "Micaela Cerqueira", "Olga Amaro"]
age_list = ["26", "26", "67"] 

#-------------------------------------------------------------------------------------------------------#

intended_action = input("If you'd like to add a new user please type '1', if you'd like to get a user's details please type '2'")

if intended_action == "1": 
   email = input("Please enter the user's email: ")
   name = input("Please enter the user's name: ")
   age = input("Please enter the user's age: ")
   input_request1(name,email,age)
else:
    if intended_action == "2":
        email = input("Please enter the user's email address: ")
        input_request2(email)

#-------------------------------------------------------------------------------------------------------#
