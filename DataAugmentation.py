# Import necessary libraries
import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
# Create an ImageDataGenerator object with various image augmentation parameters
datagen = ImageDataGenerator(
    rotation_range=40,             # Rotate the image by a random angle within the specified range (degrees)
    width_shift_range=0.2,         # Shift the width of the image by a fraction of total width
    height_shift_range=0.2,        # Shift the height of the image by a fraction of total height
    shear_range=0.2,               # Apply shear transformation by a fraction
    zoom_range=0.2,                # Zoom into the image by a random factor
    horizontal_flip=True,          # Flip the image horizontally
    fill_mode='nearest'            # Fill in newly created pixels after rotation or shifting
)
# Load an image from file (in this case, "Augmentimage.jpg")
image = load_img("Augmentimage.jpg")
# Convert the image to a NumPy array
x = img_to_array(image)
# Reshape the array to have a batch dimension (1, height, width, channels)
x = x.reshape((1,) + x.shape)
# Define the directory where augmented images will be saved
save_to_dir = 'Augment'
# Create the directory if it doesn't exist
if not os.path.exists(save_to_dir):
    os.makedirs(save_to_dir)
# Initialize a counter variable
i = 0
# Generate augmented images using the ImageDataGenerator and save them to the specified directory
for batch in datagen.flow(x, batch_size=1, save_to_dir='Augment', save_prefix='Ram', save_format='jpeg'):
    i += 1
    # Limit the number of augmented images to be generated (in this case, 20)
    if i > 20:
        break
