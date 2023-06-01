import cv2
import numpy as np

# Create a black image
image_size = 400
image = np.zeros((image_size, image_size, 3), dtype=np.uint8)

# Define the colors for different parts of Iron Man's face
red_color = (0, 0, 255)
yellow_color = (0, 255, 255)

# Define the face contour points
face_points = np.array([[120, 120], [280, 120], [200, 280]], np.int32)

# Define the eye points
left_eye_center = (160, 180)
left_eye_radius = 20

right_eye_center = (240, 180)
right_eye_radius = 20

# Define the mouth points
mouth_points = np.array([[180, 240], [220, 240], [200, 260]], np.int32)

# Start the drawing loop
while True:
    # Clear the image
    image.fill(0)

    # Draw Iron Man's face contour
    cv2.polylines(image, [face_points], True, red_color, thickness=2)

    # Draw Iron Man's eyes
    cv2.circle(image, left_eye_center, left_eye_radius, yellow_color, thickness=-1)
    cv2.circle(image, right_eye_center, right_eye_radius, yellow_color, thickness=-1)

    # Draw Iron Man's mouth
    cv2.polylines(image, [mouth_points], True, red_color, thickness=2)

    # Display the image
    cv2.imshow("Iron Man Face", image)

    # Wait for key press
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()