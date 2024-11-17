import cv2
import numpy as np
import matplotlib.pyplot as plt

def compare_and_visualize(image1_path, image2_path, output_path="diff_visualization.png"):
    # Load the images
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # Resize the second image to match the first if dimensions differ
    if img1.shape != img2.shape:
        print(f"Resizing image2 from {img2.shape} to {img1.shape}")
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))  # Resize to match img1 dimensions

    # Compute the absolute difference
    diff = cv2.absdiff(img1, img2)

    # Convert the difference image to grayscale
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Threshold the difference to highlight significant changes
    _, thresh = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)

    # Find contours of the differences
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on a copy of the original image
    diff_overlay = img1.copy()
    cv2.drawContours(diff_overlay, contours, -1, (0, 0, 255), 2)  # Red contours

    # Save and visualize the results
    cv2.imwrite(output_path, diff_overlay)

    # Plot and show the original, difference, and overlay images
    plt.figure(figsize=(12, 8))
    plt.subplot(1, 3, 1)
    plt.title("Image 1")
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.title("Image 2")
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.title("Differences Highlighted")
    plt.imshow(cv2.cvtColor(diff_overlay, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    # Return the mean difference as a value
    mean_diff = np.mean(gray_diff)
    return mean_diff

# Example usage
image1 = "screenshots/3Fe3V-73b700e9ffb6.png"
image2 = "screenshots/captivation.agency-2024-11-17_17-22-15-compressed.webp"
output_diff_image = "difference_visualization.png"

difference_value = compare_and_visualize(image1, image2, output_diff_image)
print(f"Mean pixel difference: {difference_value}")
