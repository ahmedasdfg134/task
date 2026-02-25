

This project implements a simple feed-forward neural network with:
- 2 input neurons
- 1 hidden layer (2 neurons)
- 1 output neuron
- tanh activation function

## Network Diagram

```
x1 ----\
        ( Hidden Neuron 1 ) ----\
x2 ----/                         \
                                   ( Output )
x1 ----\                         /
        ( Hidden Neuron 2 ) ----/
x2 ----/
```
)

        ( Hidden Neuron 2 ) ----/
x2 ----/
```

## Description
Weights are randomly initialized in the range [-0.5, 0.5].  
Bias values:
- b1 = 0.5 (hidden layer)
- b2 = 0.7 (output layer)

The program performs a forward pass and prints the network output.
