shipping.py

#package_weight variable will store the customer's package weight
package_weight = 20

#ground_flat contains the flat charge for ground shipping 
ground_flat = 20.00

#defined ground_shipping function to calculate cost of ground shipping

def ground_shipping(weight):
  if weight <= 2.00:
    return ((weight * 1.50) + ground_flat)
  elif weight > 2.00 and weight <= 6.00:
    return ((weight * 3.00) + ground_flat)
  elif weight > 6.00 and weight <= 10.00:
    return ((weight * 4.00) + ground_flat)
  else:
    if weight > 10.00:
      return ((weight * 4.75) + ground_flat)

calc_ground = ground_shipping(package_weight)

#print(ground_shipping(package_weight))

#ground_premium_flat stores the flat value for ground premium shipping
ground_premium_flat = 125.00

#As input by the user is needed and the approach to resolving this issue
#Is to create three functions this second function nullifies the value
#Of the weight variable by multiplying it by 0

def ground_premium(weight):
  return ((weight * 0) + 125.00)

calc_premium = ground_premium(package_weight)

#print(ground_premium(package_weight))

def drone_shipping(weight):
  if weight <= 2.00:
    return (weight * 4.50)
  elif weight > 2.00 and weight <= 6.00:
    return (weight * 9.00)
  elif weight > 6.00 and weight <= 10.00:
    return (weight * 12.00)
  else:
    if weight > 10.00:
      return (weight * 14.25)

calc_drone = drone_shipping(package_weight)

# print(drone_shipping(package_weight))

print("Thanks for using our service! the following shipping methods are available: \n","\nGround Shipping: ", calc_ground, "\nGround Shipping Premium: ", calc_premium, "\nDrone Shipping: ", calc_drone, "\n")
print("The cheapest fare available is: ", min(calc_ground, calc_premium, calc_drone), "\n \nWould you like to proceed?")



