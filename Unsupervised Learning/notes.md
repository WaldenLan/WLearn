[TOC]

## Common Unsupervised Learning Algorithms and Corresponding Tricks 

### General
* Common categories:
    - Clustering: Find the inherent groupings in the data: eg. Group the customers by their purchasing behaviors.
    - Association: Find the inherent association in the data: eg. People who buy X may also buy Y at the same time.

### Autoencoder
* Generalizing Motivation:
    - It gives low reconstruction error on test examples from the same distribution as the training examples, but generally high reconstruction error on samples randomly chosen from the input space.
* Overcomplete:
    - Intro: Have more hidden units than inputs.
    - Pros: Experiments proved to have better classification performance.
* Variation:
    - Sparse Autoencoders
    - Denoising Autoencoders
        + stochastic corruption process
            * Randomly select subsets from inputs, and make them zero.
            * Let the Autoencoders learn from the un-corrupted inputs to predict the corrupted ones. To make the Autoencoders more robust.
        + Denoising is good because you distort the data and add some noise in it that can help in generalizing over the test set.

* Application:
    - Pretrain the DNN, apply the W and b trained from the Autoencoders instead of randomly initializing them.
        + Paper experimented.
    - One-class classifier:
        + Prepare the data samples of one class, fully-train the AE, and get a threshold for the reconstructed error. Then for new test datasets, we test it through the previously-trained AE, then judge if the new sample belongs to this class by comparing the reconstructed error with the threshold.
        + But it just indicates the passed new samples have the similar features to the one class. It doesn't mean it just belongs to this class. Other not-considered classes are still possible. 
    - Compress the raw data, and extract useful features.

* Reference
    - http://deeplearning.net/tutorial/dA.html#autoencoders

### Tricks

### Plan
* 4.9:      Unsupervised Learning Overview + BP diving
* 4.16:     Autoencoder


### Others 

### Common Interview Questions

### Questions

### Reference
* [1] http://www.tuicool.com/articles/fYF3MrE