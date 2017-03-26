[TOC]

## Basics and Tuning Techniques of General Neural Networks

### History
* Perceptron model:
    - Bias Unit in the modern NN is just the original threshold in this old model.
    - You can think of the bias as a measure of how easy it is to get the perceptron to output a 1.[1]
    - Initially, the perceptron model is just like another kind of NAND logic gate. But we can devise learning algorithms to tune the W and b automatically such that break the traditional gates restriction such as the gate must be layed out and fixed, while the perceptron model can change the perceptron and even break the conventional gate types.
    - For historical reasons, such multiple layer networks are sometimes called multilayer perceptrons or MLPs, despite being made up of sigmoid neurons, not perceptrons.  

### General
* Why minimizing the quadratic cost instead of maximizing the correct classification No. ?
    -  The problem with that is that the number of images correctly classified is not a smooth function of the weights and biases in the network. For the most part, making small changes to the weights and biases won't cause any change at all in the number of training images classified correctly.
* Why applying Gradient Descent methods instead other variation?
    - Proper running time and computation cost, other methods have to calculate second partial derivatives, which have too many combinations to compute.
* Why using Stochastic Gradient Descent:
    - Original version: To compute the gradient ∇C we need to compute the gradients ∇Cx separately for each training input, x, and then average them, ∇C=(1/n)∑x∇Cx. That will take a lot of time when the training datasets are big.
    - This version: Do kind of approximation, and select mini-batch randomly from the overall datasets until all the datasets are exausted. => Fast and good performance.
    - Epoch: Similar to episode, iteration times.
* Variation for the scaling of the cost function and of mini-batch updates to the weights and biases:
    - Sometimes the (1/n) or (1/m) in the cost function will be omitted when we don't know the size of the dataset in advance. eg. Real, dynamic datasets. => Very useful.
* Why when the output is far from the desired, the learning rate is very slow?
    - It comes from both the cost function and the activation function. See the example provided in this link: http://neuralnetworksanddeeplearning.com/chap3.html#the_cross-entropy_cost_function
    - Solution: Apply a different cost function (cross-entropy cost function).
* Cross-entropy:
    - Why it's regarded as a cost function?
        + Non-negative
        + Close to 0 when output is close to the expected label:
            * Note: It's based on the assumption that the desired outputs are all either 0 or 1, which is the usual case for solving classification problems. Otherwise, the cross-entropy result won't be close to 0.
    - Why it's good?
        + The larger the error (output-expected_label) is, the faster the learning rate is, which is not controlled by the derivative of the sigmoid function (actually cross-entropy is just derived when we want to eliminate this derivative term by calculus).
    - When do we need this cost function?
        + In fact, the cross-entropy is nearly always the better choice, provided the output neurons are sigmoid neurons.
    - Why important?
        + Closely related to *neuron saturation*, which is an important problem in neural nets.
    - What it means?
        + Indicate how surprise we are regarding to the output result. We get low surprise if the output is what we expect, and high surprise if the output is unexpected. [What surprise means is covered in Information Theory]
* Softmax:
    - To be dived: http://neuralnetworksanddeeplearning.com/chap3.html#softmax
* Overfitting and Regularization:
    - How to determine the overfitting point?
        + We get it by refering to the test data prediction accuracy graph instead of the cost graph because what we really care is the accuracy.
    - Detection:
        + By accuracy visualization: when accuracy on test data stop increasing or the training accuracy also stops.

* Random Initialization of the weight matrix *W* and *b*:
    - Motivation: symmetry breaking
    - Behavior: If all the parameters are initialized by the same values, then for all the hidden layers, for any input *x* we have $$a_{1}=a_{2}=....a_{m}$$ for any hidden layer in the NN.
* Regularization:
    - Motivation: To avoid the overfitting.
    - Behavior: Add a weight decay item with a decaying parameter $$\lambda$$ to the cost function.
* Mini-Batch:
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