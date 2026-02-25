import numpy as np

def tanh(x):
    return np.tanh(x)

# inputs
x = np.array([0.6, 0.1])

# random weights in [-0.5, 0.5]
np.random.seed(0)
W1 = np.random.uniform(-0.5, 0.5, (2, 2))
W2 = np.random.uniform(-0.5, 0.5, (2, 1))

# biases
b1 = 0.5
b2 = 0.7

# forward pass
z1 = np.dot(x, W1) + b1
h = tanh(z1)

z2 = np.dot(h, W2) + b2
y = tanh(z2)

print("Hidden layer output:", h)
print("Network output:", y)
