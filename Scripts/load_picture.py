import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pathlib
import IPython.display as display
from PIL import Image

AUTOTUNE = tf.data.experimental.AUTOTUNE

# Download .zip directory of images
data_dir = tf.keras.utils.get_file(
    origin="https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz",
    fname="flower_photos",
    untar=True,
)
data_dir = pathlib.Path(data_dir)

# Count numbers of images in the directory previously download
image_count = len(list(data_dir.glob("*/*.jpg")))
print(image_count)

# Present CLASS_NAME of each directory of images
CLASS_NAMES = np.array(
    [item.name for item in data_dir.glob("*") if item.name != "LICENSE.txt"]
)
print(CLASS_NAMES)

# Display 3 images
roses = list(data_dir.glob("roses/*"))
for image_path in roses[:3]:
    display.display(Image.open(str(image_path)))

# using keras.preprocessing to rescale images
image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0 / 255)

# Parameters of lot
BATCH_SIZE = 32
IMG_HEIGHT = 224
IMG_WITDH = 224
STEPS_PER_EPOCh = np.ceil(image_count / BATCH_SIZE)

# Rules for data training
train_data_gen = image_generator.flow_from_directory(
    directory=str(data_dir),
    batch_size=BATCH_SIZE,
    shuffle=True,
    target_size=(IMG_HEIGHT, IMG_WITDH),
    classes=list(CLASS_NAMES),
)

# Batch inspection
def show_batch(image_batch, label_batch):
    plt.figure(figsize=(10, 10))
    for n in range(25):
        ax = plt.subplot(5, 5, n + 1)
        plt.imshow(image_batch[n])
        plt.title(CLASS_NAMES[label_batch[n] == 1][0].title())
        plt.axis("off")


image_batch, label_batch = next(train_data_gen)
show_batch(image_batch, label_batch)

