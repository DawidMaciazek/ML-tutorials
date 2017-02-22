from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


class MinstTester:

    def __init__(self):
        self.mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
        self.x = tf.placeholder(tf.float32, [None, 784])

        self.W = tf.Variable(tf.zeros([784, 10]))
        self.b = tf.Variable(tf.zeros([10]))

        self.y = tf.nn.softmax(tf.matmul(self.x, self.W) + self.b)
        self.y_ = tf.placeholder(tf.float32, [None, 10])

        self.cross_entropy = tf.reduce_mean(-tf.reduce_sum(self.y_ * tf.log(self.y), reduction_indices=[1]))
        self.train_step = tf.train.GradientDescentOptimizer(0.5).minimize(self.cross_entropy)
        self.sess = tf.InteractiveSession()

        tf.global_variables_initializer().run()


    def train(self, steps=1000):

        for step in range(steps):
            batch_xs, batch_ys = self.mnist.train.next_batch(100)
            self.sess.run(self.train_step, feed_dict={self.x: batch_xs, self.y_: batch_ys})


    def check_prediction(self, look_range=None):
        correct_prediction = tf.equal(tf.argmax(self.y,1), tf.argmax(self.y_,1))

        correct_list = self.sess.run(correct_prediction, feed_dict={self.x: self.mnist.test.images, self.y_: self.mnist.test.labels})

        if look_range is not None:
            print(correct_list[look_range[0]:look_range[1]])
            for i in range(look_range[0], look_range[1]):
                if not correct_list[i]:
                    self.show_image(i)

        #accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        #print(self.sess.run(accuracy, feed_dict={self.x: self.mnist.test.images, self.y_: self.mnist.test.labels}))
        #print(self.sess.run(accuracy, feed_dict={self.x: self.mnist.test.images, self.y_: self.mnist.test.labels}))

    def show_image(self, image_index):
        pixels = self.mnist.test.images[image_index].reshape((28, 28))

        label = self.mnist.test.labels[image_index]
        plt.title('Label is {label}'.format(label=label))
        plt.imshow(pixels, cmap='gray')
        plt.show()


mtest =  MinstTester()
mtest.train(1000)
mtest.check_prediction([950,1000])

