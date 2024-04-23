import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, num_epochs=100):
        self.weights = np.zeros(input_size)
        self.bias = 0
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs

    def predict(self, inputs):
        linear_combination = np.dot(self.weights, inputs) + self.bias
        activation = np.where(linear_combination > 0, 1, 0)
        return activation

    def train(self, inputs, labels):
        for epoch in range(self.num_epochs):
            for x, y in zip(inputs, labels):
                prediction = self.predict(x)
                error = y - prediction
                self.weights += self.learning_rate * error * x
                self.bias += self.learning_rate * error
