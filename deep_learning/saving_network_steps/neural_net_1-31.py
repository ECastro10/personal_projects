import tensorflow as tf

#after the training, save_name_function

# W = tf.Variable(weights, dtype, name=)
W = tf.Variable([[1, 3, 5], [5, 9, 10]], dtype=tf.float32, name='weights')
b = tf.Variable([[2, 3, 19]], dtype=tf.float32, name='biases')


#to initialize all variables
init = tf.initialize_all_variables()

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    save_path = saver.save(sess, "my_network/previous_net.ckpt")
    print("Saved to path: ", save_path)






'''

2x3 grid    3x1 grid

1 3 5         2
5 9 10        3
              19
< 2 3 19 >

The idea is to not modify the already set grid. Review linear algebra

'''
