import matplotlib.pyplot as plt
import tensorflow as tf
import numpy
import sys

# Déclaration de variables
string = tf.Variable("this is a string", tf.string)
number = tf.Variable(365, tf.int16)
floating = tf.Variable(1.618, tf.float64)

# Dimensions des tenseurs
rank_tensor1 = tf.Variable(["test", "ok", "ah", "oh"], tf.string)
rank_tensor2 = tf.Variable([["test", "ok"], ["test", "yes"]], tf.string)

print(tf.rank(rank_tensor2))
print(tf.shape(rank_tensor2))

# redimensionnement de tenseur
tensor1 = tf.ones([1, 2, 3])
tensor2 = tf.reshape(tensor1, [2, 3, 1])
tensor3 = tf.reshape(tensor2, [3, -1])

print("\n Tensor1= ", tensor1)
print("\n Tensor2= ", tensor2)
print("\n, Tensor3= ", tensor3)

# Exemple

t = tf.zeros([5, 5, 5, 5])
print(t)
t = tf.reshape(t, [625])
print(t)
