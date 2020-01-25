
#Create a list
cars = ['BMW','Mercedes','Toyota', 'Kia']

#Print the list to demonstrate how we can use indexs to display list values
print("\n----Learning Lists----")
print("\nPrint the list using indeces one by one.")
print(cars)
print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])

#Print to show how we can also ue negative values as indeces 
print("\nNow run through list backwards.")
print(cars[-1])
print(cars[-2])
print(cars[-3])
print(cars[-4])


#Replace a value in a list by direct index reference
print("\nReplace Index 0 (the first) with 'Jag'")
cars[0] = "Jag"
print(cars)

#Append (add to the end) of a list a certain value
print("\nappend() the list with 'BMW'")
cars.append("BMW")
print(cars)

#Insert a record at a specific index
print("\ninsert() a new record at index 3.")
cars.insert(3,"GMC")
print(cars)

#Remove a value from a specific index
print("\nRemove object at specific index 3")
del cars[3]
print(cars)

#Pop an item off the list store its value for later use
print("\npop() an item off the list and use its value later.")
popped_item = cars.pop(0)
print(popped_item + " has been popped.")
print(cars)

#Remove an item by its name in the list
print("\nremove() an item by name, Kia.")
cars.remove("Kia")
print(cars)

#Sort a list alphabetically
print("\nsort() the list alphabetically.")
cars.sort()
print(cars)

#Sort a list alphabetically reversed
print("\nsort(reverse=True) the list in reverse.")
cars.sort(reverse=True)
print(cars)

#Use sorted to sort only for display purposes
print("\nUse sorted() to sort only for display purposes")
print(sorted(cars))
print(cars)

#reset the list
print("\nReset the list")
cars = ['BMW','Mercedes','Toyota', 'Kia']
print(cars)

#Sort a list in reverse
print("\nSort a list in reverse()")
cars.reverse()
print(cars)

#Find the length of a list
print("\nFind the length of a list.")
print(cars)
print(len(cars))

#Looping through a list
print("\nLoop through the list.")
for car in cars:
    print(car)

#Loop through a numerical list using range (Remember that it will only run UP TO the last number in the range.)
print("\nLoop through a numerical list using range.")
for x in range(1,5):
    print(x)

#Create a list using range
print("\nCreate a list using range().")
range_list = list(range(1,5))
print(range_list)

#Create a list of even numbers using range (2 to 11, in intervals of 2)
print("\nCreate a list of even numbers using range().")
range_even = list(range(2,11,2))
print(range_even)

#Populate a list with squared values based on a range
print("\nPopulate a list with squared values based on numbers from a range.")
squared = []
for x in range(1,11):
    squared.append(x**2)
print(squared)

#For the data lovers, MIN, MAX and SUM
print("\nShow the use of min, max and sum on a list")
print("print(min(squared))")
print(min(squared))
print("print(max(squared))")
print(max(squared))
print("print(sum(squared))")
print(sum(squared))




