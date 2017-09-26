##Ada's Drones Program
##
## 1.Gather data on the amount of each drone type
## 2.Use the input to add a specific amount to each varible in a for loop as
##   in a range from 0,drone_amount
## 3.Print the results to the user
##
##
####################################################

##initialize variables
camera = 0
rotors = 0
motors = 0
wireft = 0.0

#Gathers input
print("------Welcome to Ada's Drones-------")
try:
    basic      = int(input("How many basic drones? "))
except ValueError:
    print('Please input an integer with no decimals.')
try:
    good = int(input("How many good drones? "))
except ValueError:
    print('Please input an integer with no decimals.')
try:
    ridiculous = int(input("How many ridiculous drones? "))
except ValueError:
    print('Please input an integer with no decimals.')
#calculates results
for i in range(0,basic):
    rotors  += 4
    motors  += 2
    wireft  += 4.2
for i in range(0,good):
    rotors  += 4
    motors  += 4
    camera += 1
    wireft  += 9
for i in range(0,ridiculous):
    rotors  += 8
    motors  += 12
    camera  += 5
    wireft  += 22.4

#prints results
print()
print("You will need", rotors, "rotors")
print("You will need", motors, "motors")
print("You will need", camera, "cameras")
print("You will need", wireft, "feet of wire")
