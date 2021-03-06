## Basics with Tensorflow


### Getting Started With TensorFlow

* Tensorflow Core
    - The lowest level API, should better be studied first --- helpful for understanding high-level ones.
* Tensorflow Computational Graph
    - Graph Building Stage is separated from the Running Stage, thus all the *nodes* won't be evaluated until the *session.run(...)* is executed.
* Important Concepts in Tensorflow:
    - Tensors: 
        + Primitive array values such as: 1, [1], [[1], [2]]
        + Rank: Dimension of the primitive array
        + Shape: Size of the primitive array
    - Nodes:
        + Basic computational unit, which will be evaluated when *session.run(...)* is executed.
    - Placeholders: 
        + Input parameters, which will be provided values and fed to the model later.
    - Variables:
        + Trainable parameters to adjust the performance of the model.

### MNIST For ML Beginners

* How does TensorFlow handle the overhead to do efficient matrix operation such as with NumPy, which runs the actual operation outside Python and requires lots of data transfer?
    - TensorFlow also does its heavy lifting outside Python, but it takes things a step further to avoid this overhead. Instead of running a single expensive operation independently from Python, TensorFlow lets us describe a graph of interacting operations that run entirely outside Python. (Approaches like this can be seen in a few machine learning libraries.)
    - [!!!!] Still problematic, because we always need two data transfer???
