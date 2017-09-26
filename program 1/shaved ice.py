########################################################################
##
## CS 101
## Program #3
## Aaron Darrah
## add522@mail.umkc.edu
##
## PROBLEM: A poor man would like to make a shave ice stand and would like
##          to simulate how the shave ice stand would do over the course
##          of ten days
##          
## ALGORITHM : 
##Import random module
##Initialize Keep_playing to True
##While Keep_playing is true
##	Budget is 5
##	Cup_cost is .5
##	For day in range from 1 to 10
##		Temp is random.randint from 70 to 100
##		If random.randint from 1 to 10 is 1
##			Rain is True
##			Say it is temp degrees and it is raining
##		Else
##			Say it is temp degrees and isn’t raining
##		Price is 0
##		Cups is 0
##		While price is 0
##			Ask how much you want to charge per cup and assign it to price
##			If price is less than 0
##				Say you have to charge zero or more
##		While cups*cup_cost is greater than budget
##                    While cups is 0
##				Ask how many cups they want to make and assign it to cups
##				If cups is less than 0
##					Say you have to make zero or more cups
##			If cup_cost*cups is greater than budget
##				Say you cant make more cups than you have money to make
##				While cups is 0
##					Ask how many cups they want to make and assign it to cups
##					If cups is less than 0
##						Say you have to make zero or more cups
##		Max_customers is temp-70*.5/price
##		If raining
##			Max_customers is max_customers times one half
##		Customers is random.randint from 0 to max_customers
##		Cups_sold is customers minus the difference between customers and cups
##		Budget is budget minus the difference of price times cups_sold minus the product of cups and cup_cost
##		Say you sold cups_sold and earned customers times cups_sold and you have budget dollars left
##	Ask if they want to continue and assign to continue
##	If continue is y or yes
##		Keep_playing is True
##	Elif continue is n or no
##		Keep_playing is False
##	Else 
##		Ask if they want to continue y or n
## 
## 
## ERROR HANDLING: None
##
########################################################################
import random
import math
keep_playing = True

#loop for continuation of game
while keep_playing:
    budget = 5
    cup_cost = .5
    rain = False

    #loop for the ten day cycle
    for day in range(1,11):
        print("Day", day)
        if budget == 0:
            print('You are out of money')
            break

        #determines the weather for the day
        temp = random.randint(70,100)
        if random.randint(1,10) == 1:
            rain = True
            print('It is', temp,"degrees and it's raining")
        else:
            print ('It is', temp,"degrees and clear")

        #gets input to price the cups   
        price = -1
        while price < 0:
            price = float(input("How much do you want to charge per cup?"))
            if price < 0:
                print("You must charge zero or more for a cup")

        #gets input to make cups        
        cups = -1
        while cups < 0:
            cups = int(input("How many cups would you like to make?"))
            if cups < 0:
                print("You cannot make less than zero cups")

        #stops the user from making more cups than he has money to make
        while (cups * cup_cost) > budget:
            print("You do not have the money to make that many cups.")
            cups = int(input("How many cups would you like to make?."))

        #determines the maximum customers for the day
        if price > 0:
            max_customers = ((temp-70) *.5) / price
        else:
            max_customers = 0

        #randomly generates the actual amount of customers for the day    
        customers = random.randint(0,int(max_customers)) 
        if rain:
            customers *= .5

        #determines how many cups were sold    
        if cups > customers:
            cups_sold = customers
        else:
            cups_sold = cups

        #gives the user a print-out of how their stand did that day    
        print("You sold", cups_sold, "today and made", cups_sold * price,"dollars.")
        budget += (cups_sold *price) - (cups*cup_cost)
        print("You have", budget,"dollars left\n")

    #gets input from the user on the continuation of the game    
    while True:
        cont = (input("Do you want to keep playing Y/N?")).upper()
        if cont == "Y":
            keep_playing = True
            print("\nNew Game\n")
            break
        elif cont == "N":
            keep_playing = False
            break
        else:
            print("Please enter Y or N")