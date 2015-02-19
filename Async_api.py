import time

# delay is in seconds
class ApiManager(object):
    def __init__(self, allowed, delay):
        self.ncalls = 0
        self.last_call = 0
        self.queue = []
        self.allowed = allowed
        self.delay = delay

    def call_api(self, cur_input):
        print("Api Called: " + cur_input)

    def call_on_queue(self):
        for val in self.queue:
            if self.ncalls < self.allowed:
                self.call_asynchronus(self.queue.pop(self.queue.index(val)))
        
    def call_asynchronus(self, cur_input):
        if self.last_call == 0:
            self.last_call = time.time()
        if time.time() - self.last_call < self.delay:
            if self.ncalls < self.allowed:
                self.call_api(cur_input)
                self.ncalls += 1
            else:
                self.queue.append(cur_input)
                while len(self.queue) > 0:
                    if(time.time() - self.last_call > self.delay):
                        self.ncalls = 0
                        self.last_call = time.time()
                    else:
                        self.call_on_queue()
                        if self.ncalls >= self.allowed:
                            print("time remaining: " + str(60 - (time.time() - self.last_call)))
        else:
            self.ncalls = 1
            self.call_api(cur_input)
            self.last_call = time.time()
            
    
