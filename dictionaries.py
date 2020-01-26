#Dictionarys store keys and definitions

#Making a simple dictionary
print("We make a simple dictionary and print the values.")
alien = {
    'color': 'green',
    'size': 'medium'
}
print(alien['color'])
print(alien['size'])

#We can add more data to our dictionary
print("\nWe add more data to our dictionary.")
alien['height'] = 10
alien['weight'] = 100
print(alien)

#We can change values after they exist
print("\nWe edit values inside our dictionary.")
alien['color'] = 'purple'
alien['size'] = 'large'
print(alien)

#we can make set values for our alien and then produce information based on it
alien['x-cord'] = 0
alien['y-cord'] = 10
alien['speed'] = 'fast'

print("\nThe original alien position is " + str(alien['x-cord']) + "X and " + str(alien['y-cord']) + "Y.")

if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#Modify the dicionary
alien['x-cord'] = alien['x-cord'] + x_increment
print("\nThe new alien position is " + str(alien['x-cord']) + "X and " + str(alien['y-cord']) + "Y.")

#We can change the speed definition and cause it to modify the location
print("\nIf we reset the position to 0 and change the speed we can see the result.")
alien['speed'] = 'medium'
alien['x-cord'] = 0

if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#Modify the dicionary
alien['x-cord'] = alien['x-cord'] + x_increment
print("\nThe new alien position is " + str(alien['x-cord']) + "X and " + str(alien['y-cord']) + "Y.")

#Remove a key
print("\nRemove the size key.")
print(alien)
del alien['size']
print(alien)

#Loop through our dictionary
print("\nLoop through a new dictionary.")
web_user = {
    'username': 'Goober',
    'email': 'goober@goobmail.com'
}

for key, value in web_user.items():
    print("Key: " + str(key))
    print("Value: " + str(value))

#By default we can loop only the keys (implicit)
print("\nBy default we can loop the keys.")
for key in web_user:
    print(key)

#explicit
print("\nWe can explicitly loop through keys")
for key in web_user.keys():
    print (key)

#Sort the dictionary
print("\nSort the dictionary in a loop")
for key in sorted(web_user.keys()):
    print (key)

#Print only the values
print("\nPrinting the values")
for values in web_user.values():
    print(values)

#Make multiple aliens and store them in a list
print("We make multiple aliens using a loop and store them in a list")

aliens = []
for x in range(30):
    new_alien = {'color': 'green', 'speed': 'medium', 'weight': 'heavy'}
    aliens.append(new_alien)

for x in aliens[:5]:
    print(x)
print("Total aliens created: " + str(len(aliens)))

for alien in aliens[0:4]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'fast'
        alien['weight'] = 'light'

#Put a list inside a dictionary
pizza = {
    'crust': 'thin',
    'toppings': ['pepperoni', 'bacon', 'green pepper']
}
print("\nYou ordered a " + pizza['crust'] + "-crust with the following toppings:")
for x in pizza['toppings']:
    print("\t" + x)


