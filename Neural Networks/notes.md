[TOC]

## Basics and Tuning Techniques of General Neural Networks

### General
* Random Initialization of the weight matrix *W* and *b*:
    - Motivation: symmetry breaking
    - Behavior: If all the parameters are initialized by the same values, then for all the hidden layers, for any input *x* we have $$a_{1}=a_{2}=....a_{m}$$ for any hidden layer in the NN.
* Regularization:
    - Motivation: To avoid the overfitting.
    - Behavior: Add a weight decay item with a decaying parameter $$\lambda$$ to the cost function.
* Mini-Batch:
* Stochastic Gradient Descent:
* top-k error rate:
    - The proportion of test set examples whose correct label is not among the top-k predictions of the network.

### Tricks
* A better choice of cost function, known as the cross-entropy cost function
* Four so-called "regularization" methods (L1 and L2 regularization, dropout, and artificial expansion of the training data), which make our networks better at generalizing beyond the training data
    - L1 Regularization:
    - L2 Regularization:
    - Dropout:
    - Artificial expansion of the training data:
    
* A better method for initializing the weights in the network
* A set of heuristics to help choose good hyper-parameters for the network.


### Forward Pass Algorithm


### BackPropagation Algorithm


### Common Interview Questions


### Questions
* Why matrix operation is helpful for computational efficiency?
