#EVEN Number Or ODD Number:

while True:
	print("Enter 'x' for exit.")
	val =(raw_input("Enter any number: "))
	if val == "x":
			break
	try:
		val =float(val)

		
	except ValueError:
		print "Plz Enter Numbers Only"
		
	
	if val%2 ==0:
		print "Number is Even "
	elif val%2 != 0:
		print "Number is Odd"
	else:
		print "Plz Enter Numbers Only"

		
	
