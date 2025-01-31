import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

### Imported modules above ###

#Fetched current date and time below 
current_time = dt.datetime.now().time()
current_date = dt.date.today()

###Converted current date (year) to str and sliced it to only contain the year###
current_year_str = str(current_date)
year_sliced = current_year_str[0:4]
#Generate a random number between 0 and 2025#
random_year = randint(0, 2025)

###Calculate the absolute difference between the current year and the random year###
year_difference_calc = int(year_sliced) - random_year
#print(year_difference_calc)
abs_year = abs(year_difference_calc)
#print(abs_year)
# print(random_year)

###Established a base cost in decimal and a cost multiplier, cost multiplier will be multiplied by the absolute difference between the current year and the random year and then added to the base cost###
base_cost = Decimal('1000.00')
cost_multiplier = Decimal('1.3')
total_cost = base_cost + (Decimal(str(abs_year)) * cost_multiplier)
#print(total_cost)

#established a list of possible destinations and randomly chose one using choice()#
possible_destinations = ['France', 'Germany', 'China', 'Thailand', 'Chile', 'Argentina', 'Mozambique', 'Australia', 'Canada']
destination_pick = choice(possible_destinations)
#print(destination_pick)

#Invoked generate_time_travel_message function from custom_module.py and parsed the necessary arguments#
print(custom_module.generate_time_travel_message(year=random_year, destination=destination_pick, cost=total_cost))