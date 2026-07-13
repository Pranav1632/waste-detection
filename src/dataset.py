import tensorflow as tf
from config import *

train_dataset = tf.keras.utils.image_dataset_from_directory(
    TRAIN_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True
)
test_dataset = tf.keras.utils.image_dataset_from_directory(
    TEST_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)
print(train_dataset.class_names)
print(test_dataset.class_names)
for images, labels in train_dataset.take(1):
    print(images.shape)
    print(labels.shape)