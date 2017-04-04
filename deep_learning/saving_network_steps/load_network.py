import tensorflow as tf


W = tf.Variable(tf.zeros([2, 3]), dtype=tf.float32, name='weights')
b = tf.Variable(tf.zeros([1, 3]), dtype=tf.float32, name='biases')

saver = tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess, "my_network/previous_net.ckpt")
    print('Weights: ', sess.run(W))
    print('Biases: ', sess.run(b))
