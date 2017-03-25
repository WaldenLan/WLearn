[TOC]

## Basics and Tuning Techniques of General Neural Networks

### History
* Perceptron model:
    - Bias Unit in the modern NN is just the original threshold in this old model.
    - You can think of the bias as a measure of how easy it is to get the perceptron to output a 1.[1]
    - Initially, the perceptron model is just like another kind of NAND logic gate. But we can devise learning algorithms to tune the W and b automatically such that break the traditional gates restriction such as the gate must be layed out and fixed, while the perceptron model can change the perceptron and even break the conventional gate types.
    - For historical reasons, such multiple layer networks are sometimes called multilayer perceptrons or MLPs, despite being made up of sigmoid neurons, not perceptrons.  

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
    - L2 Regularization:


    ====Next Week====

    - L1 Regularization:
    - Dropout:
    - Artificial expansion of the training data:
    
* A better method for initializing the weights in the network
* A set of heuristics to help choose good hyper-parameters [learning rate & Regularization parameter] for the network.

### Plan
* 3.26:     Overall + cross-entropy + L2-regularization
* 4.2:      NN tuning techniques left
* 4.9:      Unsupervised Learning Overview + BP diving
* 4.16:     Autoencoder


### Forward Pass Algorithm


### BackPropagation Algorithm
- It gives us detailed insights into how changing the weights and biases changes the overall behaviour of the network.

### Common Interview Questions


### Questions
* Why matrix operation is helpful for computational efficiency?


### Reference
* [1] http://neuralnetworksanddeeplearning.com/chap1.html