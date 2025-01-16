#Defined list of strings containing 0 and 1
test_list = ["1", "0", "0", "1"]

#Print list in order to observe changes later
print(test_list)

#Defined function to remove "0" from test_list
def function1():
    for zero in test_list:
        test_list.remove("0")

#Defined variable zerocount with value "0"
zerocount = "0"

#Created count variable to store count of 'zerocount' in test_list
count = test_list.count(zerocount)

#If the value in 'count' is larger than 0 function1 is called
if count > 0:
    function1()

#Final print to observe changes
print(test_list)