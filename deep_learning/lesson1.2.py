import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#60,000 training example of hand written digits
#10,000 testing examples unique
#28 x 28 pixels

#pixel is either a 0 or 1 is it white space or is it something


'''
input > weight > hidden layer 1 (activation function)  > weights > hidden layer 2 (activation function) >

send off with weights > output layer

compare the output to intended output > cost or loss function (cross entropy) how close are we

optimization function  (optimizer) > minimize cost (AdamOptimizer...SGD, AdaGrad)

backpropagation goes back to optimize weights

feed forward + backprop = epoch ---> one cycle

'''

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True) #one hot means one is hot and rest are off

# 10 classes, 0 - 9

'''
0 = 0
1 = 1
2 = 2

one hot does
0 = [1,0,0,0,0,0,0,0,0]
1 = [0,1,0,0,0,0,0,0,0]
2 = [0,0,1,0,0,0,0,0,0]
3 = [0,0,0,1,0,0,0,0,0]
'''

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10

batch_size = 100 #goes through batches of 100 features at a time

#place holding variables

#matrix is height x width y
x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float')


def neural_network_model(data):


    # ( input_data * weights ) + biases

    hidden_1_layer = {'weights': tf.Variable(tf.random_normal([784, n_nodes_hl1])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl1]))}

    hidden_2_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))}

    hidden_3_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl3]))}

    output_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                    'biases': tf.Variable(tf.random_normal([n_classes]))}


    # Model for each layer (input_data * weights) + biases

    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])

    # Goes through activation function

    l1 = tf.nn.relu(l1) # rectify linear aka threshold function

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])

    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']), hidden_3_layer['biases'])

    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']


    return output



def train_neural_network(x):


    prediction = neural_network_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(prediction,y))

    # learning rate = 0.001
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    # cycles of feed forward plus backprop

    hm_epochs = 10

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables()) # begins the session and starts running it

        #Training the data
        for epoch in range(hm_epochs):
            epoch_loss = 0

            for _ in range(int(mnist.train.num_examples/batch_size)):
                epoch_x, epoch_y = mnist.train.next_batch(batch_size)

                _, c = sess.run([optimizer, cost], feed_dict={x: epoch_x, y:epoch_y})

                epoch_loss += c
            print('Epoch', epoch, ' completed out of ', hm_epochs, ' loss: ', epoch_loss)


        # Now run through the model

        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))# returns the index value of the value in each array

        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

        print('Accuracy: ', accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))


train_neural_network(x)





