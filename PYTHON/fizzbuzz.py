# This is my first attempt to code the game fizzbuzz
# I got this idea from the following video: https://www.youtube.com/watch?v=QPZ0pIK_wsc&ab_channel=TomScott

my_list = []

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        i = "FizzBuzz"
    elif i % 5 == 0:
        i = "Buzz"
    else: 
        if i % 3 == 0:
            i = "Fizz"
    my_list.append(i)

print(my_list)

# Big success!


    