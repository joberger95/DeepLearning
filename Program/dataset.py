from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import os
import numpy as np
import matplotlib.pyplot as plt
import zipfile

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Import path to pictures
_URL = "https://"

