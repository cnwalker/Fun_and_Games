import random

def montyHall():
	#Evaluates one instance of the Monty Hall problem. Returns the given answer
	options = ['sheep1', 'car', 'sheep2']
	random.shuffle(options)
	choice = random.choice(options)
	if choice == 'sheep1':
		options.remove('sheep2')
	else:
		options.remove ('sheep1')
	options.remove(choice)
	return options[0]
	
def evaluateMontyHall(num):
	correct = 0.0
	wrong = 0.0
	for i in range(0, num):
		if montyHall() == 'car':
			correct += 1
		else:
			wrong += 1
	return str(100*(correct/(correct + wrong))) + '%'
