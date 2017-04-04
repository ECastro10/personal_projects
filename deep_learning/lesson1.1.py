import tensorflow as tf

x1 = tf.constant(5)
#x1 = tf.constant([5, 6])
x2 = tf.constant(6)

result = tf.mul(x1, x2)
print(result)

sess = tf.Session()

print(sess.run(result))

sess.close()

#Here is the correct way to run the code above

x1 = tf.constant(5)
#normally these constants would be vectors
# x1 = tf.constant([5, 6])
x2 = tf.constant(6)

result = tf.mul(x1, x2)

# the with block is best practice in this cell, cell 2 is not
with tf.Session() as sess:
    output = sess.run(result)
    print(output)

    # First build computational model

    # Then build Session