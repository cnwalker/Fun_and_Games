import random

def montyHall(switch):
# Evaluates one instance of the Monty Hall problem. Returns the answer
# Switch is true the player switches; otherwise she keeps her initial choice
        options = ['sheep1', 'car', 'sheep2']
        random.shuffle(options)
        choice = random.choice(options)
        if switch == False:
                return choice
        if choice == 'sheep1':
                options.remove('sheep2')
        else:
                options.remove ('sheep1')
        options.remove(choice)
        return options[0]
        
def evaluateMontyHall(num, switch):
# Return the percentage of times the player gets a car with the given strategy
        correct = 0.0
        wrong = 0.0
        for i in range(0, num):
                if montyHall(switch) == 'car':
                        correct += 1
                else:
                        wrong += 1
        return str(100*(correct/(correct + wrong))) + '%'
                
        
        
        
        
        
