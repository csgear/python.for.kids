import numpy as np
import tensorflow as tf 

# np.random.seed(10)
# x = np.random.normal(size=[10,10])
# y = np.random.normal(size=[10,10])

# z = np.dot(x, y)

# print(z)

# x = tf.random_normal(shape=[10,10], seed=10)
# y = tf.random_normal(shape=[10,10])
# z = tf.matmul(x, y)

# sess = tf.Session()

# with sess:
#     sess.run(z)
#     print(z.eval())
#     sess.close()


sess = tf.Session()

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

w = tf.get_variable("w", shape=[3, 1])

sess = tf.Session()

sess.run(tf.global_variables_initializer())

with sess:
    w = tf.Tensor[5,1,1]
    sess.run([w])
