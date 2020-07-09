from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import os
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Import path to pictures
_URL = "https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip"
path_to_zip = tf.keras.utils.get_file("cats_and_dogs.zip", origin=_URL, extract=True)
PATH = os.path.join(os.path.dirname(path_to_zip), "cats_and_dogs_filtered")

# Create directory for training and validation
train_dir = os.path.join(PATH, "train")
valid_dir = os.path.join(PATH, "validation")

train_cats_dir = os.path.join(train_dir, "cats")
valid_cats_dir = os.path.join(train_dir, "cats")
train_dogs_dir = os.path.join(train_dir, "dogs")
valid_dogs_dir = os.path.join(train_dir, "dogs")

# Visualize data arragement
number_cats_train = len(os.listdir(train_cats_dir))
number_cats_valid = len(os.listdir(valid_cats_dir))
number_dogs_train = len(os.listdir(train_dogs_dir))
number_dogs_valid = len(os.listdir(valid_dogs_dir))
total_train = number_cats_train + number_dogs_train
total_valid = number_cats_valid + number_dogs_valid
print("Total number cats training: ", number_cats_train)
print("Total number cats validate: ", number_cats_valid)
print("Total number dogs training: ", number_dogs_train)
print("Total number dogs validate: ", number_dogs_valid)
print("\nTotal training images: ", total_train)
print("Total validating images: ", total_valid)


# Data preparation
# Parameters of lot
BATCH_SIZE = 128
IMG_HEIGHT = 150
IMG_WITDH = 150
EPOCHS = 15

# Rescaling images
train_image_generator = ImageDataGenerator(rescale=1.0 / 255)
validation_image_generator = ImageDataGenerator(rescale=1.0 / 255)
# Parameters of the training data generator
train_data_generator = train_image_generator.flow_from_directory(
    batch_size=BATCH_SIZE,
    directory=train_dir,
    shuffle=True,
    target_size=(IMG_HEIGHT, IMG_WITDH),
    class_mode="binary",
)

# Parameters of the validation data generator
valid_data_generator = validation_image_generator.flow_from_directory(
    batch_size=BATCH_SIZE,
    directory=valid_dir,
    target_size=(IMG_HEIGHT, IMG_WITDH),
    class_mode="binary",
)


sample_training_images, _ = next(train_data_generator)


def plotImages(images_array):
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images_array, axes):
        ax.imshow(img)
        ax.axis("off")
    plt.tight_layout()
    # plt.show()


plotImages(sample_training_images[5])

# Create the models with his layers
model = Sequential(
    [
        Conv2D(
            16,
            3,
            padding="same",
            activation="relu",
            input_shape=(IMG_HEIGHT, IMG_WITDH, 3),
        ),
        MaxPooling2D(),
        Dropout(0.2),
        Conv2D(32, 3, padding="same", activation="relu"),
        MaxPooling2D(),
        Conv2D(64, 3, padding="same", activation="relu"),
        MaxPooling2D(),
        Dropout(0.2),
        Flatten(),
        Dense(512, activation="relu"),
        Dense(1),
    ]
)

model.compile(
    optimizer="adam",
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
    metrics=["accuracy"],
)

# For view all the layers of neural network
model.summary()

# Training the model
history = model.fit_generator(
    train_data_generator,
    steps_per_epoch=total_train // BATCH_SIZE,
    epochs=EPOCHS,
    validation_data=valid_data_generator,
    validation_steps=total_valid // BATCH_SIZE,
)

# Visualization of training results
acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]

loss = history.history["loss"]
val_loss = history.history["val_loss"]

epochs_range = range(EPOCHS)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label="Traingin Accuracy")
plt.plot(epochs_range, val_acc, label="Validation Accuracy")
plt.legend(loc="lower right")
plt.title("Training and Validation Accuracy")

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label="Traingin Loss")
plt.plot(epochs_range, val_loss, label="Validation Loss")
plt.legend(loc="upper right")
plt.title("Training and Validation Loss")
plt.show()

