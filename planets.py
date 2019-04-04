def weight_on_planets():
	weight = float(input('What do you weigh on earth? ')) #prompt user for weight input and cast as a float
	print('\nOn Mars you would weigh', weight * .38, 'pounds.\nOn Jupiter you would weigh', weight * 2.34, 'pounds.')
	#prints their weight on mars and jupiter using preset conversion values
   
   
if __name__ == '__main__':
   weight_on_planets()
