class Perceptron:
    def __init__(self, epoch, learning_rate):
        self.b = 0
        self.w = {}
        self.epochs = epoch
        self.learning_rate = learning_rate
        self.score = 0
    
    def inisialisasi(self,inputs):
        for i in range(len(inputs[0])):
            self.w['w'+str(i)] = 0

    def train(self,inputs,label):
        self.inisialisasi(inputs)

        for epoch in range(self.epochs):
            for input, target in zip(inputs,label):
                y_in = 0
                for index, x in enumerate(input):
                    y_in = y_in + (x*self.w['w'+str(index)])
                y_in = y_in + self.b

                aktivasi = lambda x: 1 if x>=0 else 0 #aktivasi biner
                if aktivasi(y_in) != label:
                    error = target - aktivasi(y_in)
                    for index, x in enumerate(input):
                        self.w['w'+str(index)] = self.w['w'+str(index)] + (self.learning_rate*error*x)
                    self.b = self.b + (self.learning_rate*error)
    
    def predict(self,x):
        y_in = 0
        for index, input in enumerate(x):
            y_in = y_in +(input*self.w['w'+str(index)])
        y_in = y_in + self.b
            
        aktivasi = lambda x : 1 if x >= 0 else 0 #aktivasi biner
        
        return aktivasi(y_in)
        
    
X = [[0,0],[0,1],[1,0],[1,1]]
y = [0,0,0,1]
epoch = 10
learning_rate = 1


P = Perceptron(10,1)
P.train(X,y)
P.predict([1,0])