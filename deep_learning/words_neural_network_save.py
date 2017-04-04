import tensorflow as tf
import pickle
import numpy as np
import timeit


# mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)



n_nodes_hl1 = 500

n_nodes_hl2 = 500

n_nodes_hl3 = 500



n_classes = 2

batch_size = 100

train_x, train_y, test_x, test_y = pickle.load(open('sentiment_set.pickle', 'rb'))

size = len(train_x[0])

x = tf.placeholder('float', [None, size])

y = tf.placeholder('float')


weights = tf.Variable(tf.zeros([500, 2], dtype=tf.float32, name='weights'))
biases = tf.Variable(tf.zeros([2, 423], dtype=tf.float32, name='biases'))


# def print_text(train_x):
#     count=0
#     rows=0
#
#     for i in range(0, len(train_x)):
#         rows += 1
#         for j in train_x[i]:
#             count += 1
#
#     print('Total count is: ', count)
#     print('Total rows are: ', rows)
#
#
# def get_example(train_x):
#     for i in range(0, 2):
#         print(train_x[i])
#         print('array at index {} is of size {}'.format(i, len(train_x[i])))


def neural_network_model(data):

    global weights
    global biases


    hidden_1_layer = {'weights': tf.Variable(tf.random_normal([size, n_nodes_hl1])),

                      'biases': tf.Variable(tf.random_normal([n_nodes_hl1]))}



    hidden_2_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),

                      'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))}



    hidden_3_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),

                      'biases': tf.Variable(tf.random_normal([n_nodes_hl3]))}



    output_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),

                    'biases': tf.Variable(tf.random_normal([n_classes])), }



    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])

    l1 = tf.nn.relu(l1)



    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])

    l2 = tf.nn.relu(l2)



    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']), hidden_3_layer['biases'])

    l3 = tf.nn.relu(l3)



    output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']



    return output





def train_neural_network(x):

    global weights
    global biases

    prediction = neural_network_model(x)

    # OLD VERSION:

    # cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(prediction,y) )

    # NEW:

    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))

    optimizer = tf.train.AdamOptimizer().minimize(cost)



    hm_epochs = 20

    with tf.Session() as sess:

        # OLD:

        # sess.run(tf.initialize_all_variables())

        # NEW:

        sess.run(tf.global_variables_initializer())



        for epoch in range(hm_epochs):

            epoch_loss = 0

            # for _ in range(int(mnist.train.num_examples / batch_size)):
            #
            #     epoch_x, epoch_y = mnist.train.next_batch(batch_size)
            #

            i = 0
            while i < size:
                start = i
                end = i + batch_size

                batch_x = np.array(train_x[start:end])
                batch_y = np.array(train_y[start:end])


                _, c = sess.run([optimizer, cost], feed_dict={x: batch_x, y: batch_y})

                epoch_loss += c

                i += batch_size



            print('Epoch', epoch, 'completed out of', hm_epochs, 'loss:', epoch_loss)



        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))



        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

        print('Accuracy:', accuracy.eval({x: train_x, y: train_y}))


        #----------------Save Weights & Biases--------------------#

        print(sess.run(weights))
        print(sess.run(biases))
        saver = tf.train.Saver()

        save_path = saver.save(sess, "saved_weights_for_words/previous_net.ckpt")
        print("Saved to path: ", save_path)



start_time = timeit.default_timer()
train_neural_network(x)
elapsed = timeit.default_timer() - start_time
print('Total elapsed time was: ', elapsed)
# print_text(train_y)
# get_example(train_x)