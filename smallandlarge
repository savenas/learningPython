# Learning Python
# Tomas Savenas
# ===============

import os
os.system('cls' if os.name == 'nt' else 'clear')


print('This is smallest and largest number finder application based on snake oil AI')
print('Enter Done if you want to finish the application')

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    
    if num == "Done" or num == "done" : 
    	break
    
    try:
    	num = float(num)
    	if smallest is None:
    		smallest = num
    	if largest is None:
    		largest = num
    	elif num < smallest:
    		smallest = num
    	elif num > largest:
    		largest = num
    except:
    	print('Invalid input, application aceepts only numbers')
	
print("Maximum is", largest)
print("Minimum is", smallest)
