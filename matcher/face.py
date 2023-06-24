import cv2
import face_recognition
import numpy as np

def compare_faces(image1_path, image2_path):
    # Load the images using OpenCV
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Convert the images from BGR to RGB (OpenCV uses BGR format)
    image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image2_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

    # Detect faces in the images using OpenCV
    face_locations1 = face_recognition.face_locations(image1_rgb)
    face_locations2 = face_recognition.face_locations(image2_rgb)

    if len(face_locations1) == 0:
        return "No face found in image 1"

    if len(face_locations2) == 0:
        return "No face found in image 2"

    # Extract face encodings from the images
    face1_encodings = face_recognition.face_encodings(image1_rgb, face_locations1)
    face2_encodings = face_recognition.face_encodings(image2_rgb, face_locations2)

    # Convert the face encodings to NumPy arrays
    face1_encodings = np.array(face1_encodings)
    face2_encodings = np.array(face2_encodings)

    # Compare the face encodings
    face_distances = face_recognition.face_distance(face1_encodings, face2_encodings)

    # Calculate the similarity percentage
    similarity_percentage = (1 - face_distances) * 100

    # Check if there is any match above a threshold
    threshold = 50  # Adjust this threshold based on your requirements
    if any(similarity_percentage >= threshold):
        max_similarity = max(similarity_percentage)
        return "Same person with a similarity of {:.2f}%".format(max_similarity)
    else:
        return "Different persons"

# Provide the paths to the two images you want to compare
image1_path = "Dv.jpg"
image2_path = "Webcam_2.jpeg"

# Compare the images
result = compare_faces(image1_path, image2_path)

print(result)


