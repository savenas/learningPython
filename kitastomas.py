# Learning Python
# Tomas Savenas
# ===============

import os
os.system('cls' if os.name == 'nt' else 'clear')

def computepay(h,r):
    try:
    	h = float(h)
    	r = float(r)
    	if h > 40:
    		result = h * r 
    	elif h < 40:
    		result = h * r
    except:
    	print('Invalid input, application aceepts only numbers')
    return result


hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs,rate)
print("Pay",p)