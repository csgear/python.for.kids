import tensorflow as tf
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import colors

# define parameters & global variables

BATCH_SIZE = 100 

tf.flags.DEFINE_string('train', 'tfsvm_train.csv', 
                        'File containing the traing data (label & features)') 

tf.flags.DEFINE_boolean("verbose", False, 'Produce verbose output.') 

tf.flags.DEFINE_float('svmC', 1, 'hyper-parameter for svm')

tf.flags.DEFINE_integer('num_epochs', 10, "Number of training epochs")

FLAGS = tf.flags.FLAGS



# extract data from csv file
def extract_data(filename):
    data = np.loadtxt(filename, delimiter=',')
    labels = data[:,0]
    labels = labels.reshape(labels.size,1)
    features = data[:,1:]
    return features, labels

def plot_boundary_on_data(X,Y,pred_func):
    # determine canvas borders
    mins = np.amin(X,0); 
    mins = mins - 0.1*np.abs(mins) 
    maxs = np.amax(X,0); 
    maxs = maxs + 0.1*maxs 

    ## generate dense grid
    xs,ys = np.meshgrid(np.linspace(mins[0],maxs[0],300), 
            np.linspace(mins[1], maxs[1], 300))


    # evaluate model on the dense grid
    Z = pred_func(np.c_[xs.flatten(), ys.flatten()])
    Z = Z.reshape(xs.shape)

    # Plot the contour and training examples
    plt.contourf(xs, ys, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:,0], X[:,1], c=Y.reshape(Y.size), s=50, cmap=colors.ListedColormap(['orange', 'blue']))
    plt.show()


def main(argv=None):
    print(FLAGS.train)
    print(FLAGS.verbose)

    train_data_filename = FLAGS.train
    train_data, train_labels = extract_data(train_data_filename)

    print(train_data.shape, train_data.size)
    print(train_labels.shape)

    train_labels[train_labels==0] = -1

    train_size,num_features = train_data.shape

    x = tf.placeholder('float', shape=[None, num_features])
    y = tf.placeholder('float', shape=[None, 1])

    W = tf.Variable(tf.zeros([num_features, 1]))
    b = tf.Variable(tf.zeros([1]))
    y_ = tf.matmul(x, W) + b

    # svm training step
    svmC = FLAGS.svmC 
    regularization_loss = 0.5 * tf.reduce_sum(tf.square(W)) 
    hinge_loss = tf.reduce_sum(tf.maximum(tf.zeros([BATCH_SIZE,1]), 1 - y*y_)) 
    svm_loss = regularization_loss + svmC * hinge_loss 
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(svm_loss)

    # prediction
    predicted_class = tf.sign(y_) 
    num_epochs = FLAGS.num_epochs

    with tf.Session() as sess:
        tf.initialize_all_variables().run()

        for step in range(num_epochs * train_size // BATCH_SIZE):
            offset = (step * BATCH_SIZE) % train_size

            batch_data = train_data[offset:(offset + BATCH_SIZE), :]
            batch_labels = train_labels[offset:(offset + BATCH_SIZE)]

            train_step.run(feed_dict={x:batch_data, y:batch_labels})

            print("losss : {:0.2f}".format(svm_loss.eval(feed_dict={x:batch_data, y:batch_labels})))

        eval_fun = lambda X: predicted_class.eval(feed_dict={x:X})

        plot_boundary_on_data(train_data, train_labels, eval_fun)

if __name__ == "__main__":
    tf.app.run()