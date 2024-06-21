import numpy as np



# # one input

# # random inputs
# inputs = [1, 2, 3, 2.5]
# # random weights
# weights = [0.2, 0.8, -0.5, 1.0]
# #random bias
# bias = 0.5

# # calculating bias
# output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + inputs[3] * weights[3] + bias
# print(output)





# #multiple inputs

# # random weights
# weights1 = [0.2, 0.8, -0.5, 1.0]
# weights2 = [0.5, -0.91, 0.26, -0.5]
# weights3 = [-0.26, -0.27, 0.17, 0.87]


# #random biases
# bias1 = 2
# bias2 = 3
# bias3 = 0.5


# #calculating output
# output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1,
#           inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2,
#           inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3]
# print(output)






'''
np.dot function
'''


# # one weight


# inputs = [1, 2, 3, 2.5]

# weights = [0.2, 0.8, -0.5, 1.0]

# bias = 2

# #check product.py to see what .np does
# output = np.dot(inputs, weights) + bias
# #input, output == vectors
# print(output)




# # multiple weights

# inputs = [1, 2, 3, 2.5]

# weights = [[0.2, 0.8, -0.5, 1.0],
#            [0.5, -0.91, 0.26, -0.5],
#            [-0.26, -0.27, 0.17, 0.87]]

# biases = [2, 3, 0.5]

# output = np.dot(weights, inputs) + biases
# print(output)



'''
=====================
'''

# inputs = [[1, 2, 3, 2.5],
#           [2.0, 5.0, -1.0, 2.0],
#           [-1.5, 2.7, 3.3, -0.8]]

# weights = [[0.2, 0.8, -0.5, 1.0],
#            [0.5, -0.91, 0.26, -0.5],
#            [-0.26, -0.27, 0.17, 0.87]]

# biases = [2, 3, 0.5]


# #second layer
# weights2 = [[0.1, -0.14, 0.5],
#            [-0.5, 0.12, -0.33],
#            [-0.44, 0.73, -0.13]]

# biases2 = [-1, 2, -0.5]


# #.T transposes our matrix so the 
# # index1 of the first element to mach index0 of the second element
# layer1_output = np.dot(inputs, np.array(weights).T) + biases

# layer2_output = np.dot(layer1_output, np.array(weights2).T) + biases2

# print(layer2_output)




'''
================

================
'''
#input data
np.random.seed(0)

X = [[1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]]


#define 2 hidden layers
#how to initialize layers
class layer_dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        
layer1 = layer_dense(4,5)
layer2 = layer_dense(5,2)

layer1.forward(X)
print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)