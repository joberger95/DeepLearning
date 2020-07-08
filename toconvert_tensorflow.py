import tensorflow as tf

root = tf.train.Checkpoint()
root.v1 = tf.Variable(3.0)
root.v2 = tf.Variable(2.0)
root.f = tf.function(lambda x: root.v1 * root.v2 * x)

export_dir = "/home/jordan/test_saved_model"
input_data = tf.constant(1.0, shape=[1, 1])
to_save = root.f.get_concrete_function(input_data)
tf.saved_model.save(root, export_dir, to_save)

converter = tf.lite.TFLiteConverter.from_saved_model(export_dir)
tflite_model = converter.convert()

with tf.io.gfile.GFile("model.tflite", "wb") as f:
    f.write(tflite_model)
