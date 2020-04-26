score = input("Enter score between 0 and 1.0: ")
try:
	s = float(score)
	if s>1 or s < 0 :
		print("You have to enter the score between 0 and 1.0")
	else:
		if s>=0.9:
			print("score A")
		elif s>=0.8:
			print("score B")
		elif s>=0.7:
			print("score C")
		elif s>=0.6:
			print("score D")
		elif s<0.6:
			print("score C")
except:
	print("You have to enter the score between 0 and 1.0")
