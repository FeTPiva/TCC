#https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6
#https://gist.github.com/jamesloyys/ff7a7bb1540384f709856f9cdcdee70d#file-neural_network_backprop-py

#ver2 pra xteste https://towardsdatascience.com/machine-learning-in-python-numpy-neural-network-in-9-steps-eafd0db25906
# Imports
#obs:numpy é um biblioteca pra coisas cientificas onde vc pode mexer c arrays de tamanho nnos seus valores(super matrizoes)
import numpy as np 
      
# Each row is a training example, each column is a feature  [X1, X2, X3]- 4 exemplos, 3 featurees


X=np.array(([0,0,1],[0,1,1],[1,0,1],[1,1,1]), dtype=float)
y=np.array(([0],[1],[1],[0]), dtype=float)

#valores do meu codigo la em 3 textos, e ja rolou!
x2=np.array(([0.024472049684408,0.024472049684408,0.008281573498964804, 0.3],[0,0.04040404040,0.006734006734, 0.1],[0.07290533188248095,0.04570184983677911, 0.018498367791077257, 0.4 ]), dtype=float)
y2=np.array(([1],[0],[1]), dtype=float)
#1 depre, 0 n depre



# Activation function
def sigmoid(t):
    return 1/(1+np.exp(-t))

# Derivative of sigmoid
def sigmoid_derivative(p):
    return p * (1 - p)

# Class definition
class NeuralNetwork:
    def __init__(self, x2,y2):
        self.input = x2
        self.weights1= np.random.rand(self.input.shape[1],4) # considering we have 4 nodes in the hidden layer
        self.weights2 = np.random.rand(4,1)
        self.y2 = y2
        self.output = np. zeros(y2.shape)
        
    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        return self.layer2
        
    def backprop(self):
        d_weights2 = np.dot(self.layer1.T, 2*(self.y2 -self.output)*sigmoid_derivative(self.output))
        d_weights1 = np.dot(self.input.T, np.dot(2*(self.y2 -self.output)*sigmoid_derivative(self.output), self.weights2.T)*sigmoid_derivative(self.layer1))
    
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, x2, y2):
        self.output = self.feedforward()
        self.backprop()
        

NN = NeuralNetwork(x2,y2)
print("startando...")
for i in range(3000): # trains the NN 1,000 times-EPOCAS
    if i % 100 ==0: 
        print ("for iteration # " + str(i) + "\n")
        print ("Input : \n" + str(x2))
        print ("Actual Output: \n" + str(y2))
        print ("Predicted Output: \n" + str(NN.feedforward()))
        print ("Loss: \n" + str(np.mean(np.square(y2 - NN.feedforward())))) # mean sum squared loss
        print ("\n")
  
    NN.train(x2, y2)

    
