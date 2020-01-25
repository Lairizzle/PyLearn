#Tuples are like lists but immuateble. They cannot be changed.

#Define a tuple
print("Define a tuple.")
my_tuple = (1,2,3)
print(my_tuple)

#If we try to change a tuple we wil get an error
print("\nIf we try to change a tuple we will throw an error.")
print("my_tuple[0] = 5")

#Try it and catch the error below
try:
    my_tuple[0] = 5

except TypeError:
    print("Error: We cannot change a tuple.")

