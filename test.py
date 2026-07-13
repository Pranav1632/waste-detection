import tensorflow as tf

print("TensorFlow Version:", tf.__version__)

print("Available Devices:")
print(tf.config.list_physical_devices())

print("CPU:", tf.config.list_physical_devices('CPU'))
print("GPU:", tf.config.list_physical_devices('GPU'))