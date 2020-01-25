#if statements are conditional tests.
print("We will use a basic true/false variable for our test.")
conditional_test = True
if conditional_test:
    print("Yes, it is true.")

#Let us create another conditional test using a variable
print("\nIf we set the age to 18.")
age = 18
if age < 20:
    print("This person is less than 20.")

#Else statements account for different outcomes
print("\nWe will use an else statement to check for different outcomes and change the age to 22.")
age = 22
if age < 20:
    print("This person is less than 20.")
else:
    print("This person is over the age of 20.")

#Elseif or elif in Python will allow us to add even more conditional checks
print("\nWe will use elif to add more conditional checks. We will set the age to 16.")
age = 16
if age < 5:
    print("This person is less than 20.")
elif age > 20:
    print("This person is over the age of 20.")
else:
    print("Your age is between 5 and 20")

#What if we want to test multiple things?
print("\nLet's check mutiple conditions from a list.")

flavours = ['blue','red','orange']

if 'blue' in flavours:
    print("Blue flavour exists.")
if 'red' in flavours:
    print("Red flavour exists.")
if 'purple' in flavours:
    print("Purple flavour exists.")
else:
    print("Purple does not exist.")

#Lets loop through a list and use one if statement instead of writing it many times
print("\nLet's write a loop instead of writing the same if statement over and over.")
for x in flavours:
    if x == 'orange':
        print("We are out of Orange right now, sorry!")
    else:
        print("We have " + x + " flavour in stock.")

#Lets make a list of in stock flavours and a pretend flavour request list
print("\nLet us create an inventory of flavours and a request and handle it.")
in_stock = ['blue','red','orange','green']
requested = ['blue','orange','yellow','purple']

for x in requested:
    if x in in_stock:
        print(x + " flavour is available")
    else:
        print("Sorry! " + x + " flavour is not available.")
