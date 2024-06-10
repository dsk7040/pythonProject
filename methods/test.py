from PIL import Image, ImageChops
from PIL import Image, ImageChops, ImageEnhance
import numpy as np
import time


def compare_images(image1_path, image2_path, diff_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Convert images to NumPy arrays
    np_image1 = np.array(image1)
    np_image2 = np.array(image2)

    # Check if the shapes match
    if np_image1.shape != np_image2.shape:
        print("Images have different dimensions and cannot be compared.")
        return False

    # Calculate the difference
    time.sleep(5)
    diff = np.abs(np_image1 - np_image2)

    # Check if there are any non-zero elements in the difference array
    if np.any(diff):
        print("Images are different.")

        # Save the diff image if a path is provided
        if diff_path:
            diff_image = ImageChops.difference(image1, image2)
            # enhancer = ImageEnhance.Contrast(diff_image)
            # diff_image = enhancer.enhance(2)  # Increase contrast

            # Convert to grayscale for better visibility
            diff_image = diff_image.convert('L')
            diff_image.save(diff_path)
            print(f"Difference image saved at {diff_path}")
        return False
    else:
        print("Images are the same.")
        return True


# Compare the screenshots and save the difference image
compare_images("D:\\Project Screenshots\\Baltech\\deep1 + .png", "D:\\Project Screenshots\\Baltech\\deep2 + .png", "D:\\Project Screenshots\\deep5 + .png")
