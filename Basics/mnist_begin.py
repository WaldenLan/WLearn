# Read data
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf

# Input datasets
x = tf.placeholder(tf.float32, [None, 784])

# Adjustable parameters
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Target Result
y = tf.nn.softmax(tf.matmul(x, W) + b)

# Correct results
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# Setup the training step
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# Start the session
sess = tf.InteractiveSession()
# Initialize the variables
tf.global_variables_initializer().run()
# Start the training
for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# Evaluate the training results on the test datasets
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
