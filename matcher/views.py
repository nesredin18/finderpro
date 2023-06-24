import face_recognition
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .automated import send_images_for_comparison
from thread.models import found_i,lost_i,lost_P,found_P
from django.db.models import Q
from Levenshtein import ratio
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from rest_framework.response import Response
from .models import matched_i,matched_p
import cv2
import face_recognition
import numpy as np
from PIL import Image


def fuzzy_match(string1, string2):
    if string1 and string2:
        return ratio(string1, string2)
    else:
        return 0

def match_items():
    matches = []
    for lost_item in lost_i.objects.all():

        possible_matches = found_i.objects.filter(
            Q(region=lost_item.region) |
            Q(i_type=lost_item.i_type)
            )  
        
        for found_item in possible_matches:
            sum=0
            divider=0
            if(lost_item.detail and found_item.detail):
                detail_similarity = fuzzy_match(lost_item.detail, found_item.detail)
                divider+=detail_similarity
                sum+=1
            if(lost_item.serial_n and found_item.serial_n):
                serial_similarity = fuzzy_match(lost_item.serial_n, found_item.serial_n)
                divider+=serial_similarity
                sum+=1
            if(lost_item.adress and found_item.adress):
                address_similarity = fuzzy_match(lost_item.adress, found_item.adress)
                divider+=address_similarity
                sum+=1
            if(lost_item.city and found_item.city):
                city_similarity = fuzzy_match(lost_item.city, found_item.city)
                divider+=city_similarity
                sum+=1
            if(lost_item.lost_date and found_item.lost_date):
                date_difference = abs((found_item.lost_date - lost_item.lost_date).days)
                sum+=1
                if(date_difference<=30):
                    divider+=1
            print(lost_item)
            print(found_item)
            print(divider)
            print(sum)
            # Consider matches where the details, serial number, and address are 80% similar
            if divider/sum >= 0.7:
                # You have a match, add to matches list
                matches.append((lost_item, found_item))
    return matches

def match_person():
    matches = []
    for lost_person in lost_P.objects.all():
        possible_matches = found_P.objects.filter(
            Q(region=lost_person.region) |
            Q(p_type=lost_person.p_type)|
            Q(gender=lost_person.gender)
        )  
        
        for found_person in possible_matches:
            divider=0
            sum=0
            image_similarity=0
            if(lost_person.image_url and found_person.image_url):
                image_similarity = compare_faces(lost_person.image_url, found_person.image_url)
                if(type(image_similarity)==str):
                    continue
                if(image_similarity>=60):
                    matches.append((lost_person, found_person))
                    continue
                else:
                    divider+=image_similarity/100
                    sum+=1
            if(lost_person.first_name and found_person.first_name):
                first_name_similarity = fuzzy_match(lost_person.first_name, found_person.first_name)
                divider+=first_name_similarity
                sum+=1
            if(lost_person.last_name and found_person.last_name):
                last_name_similarity = fuzzy_match(lost_person.last_name, found_person.last_name)
                divider+=last_name_similarity
                sum+=1

            if(lost_person.city and found_person.city):
                city_similarity = fuzzy_match(lost_person.city, found_person.city)
                divider+=city_similarity
                sum+=1
            if(lost_person.cloth and found_person.cloth):
                cloth_similarity = fuzzy_match(lost_person.cloth, found_person.cloth)
                divider+=cloth_similarity
                sum+=1
            if(lost_person.mark and found_person.mark):
                mark_similarity = fuzzy_match(lost_person.mark, found_person.mark)
                divider+=mark_similarity
                sum+=1
            if(lost_person.detail and found_person.detail):
                detail_similarity = fuzzy_match(lost_person.detail, found_person.detail)
                divider+=detail_similarity
                sum+=1
            if(lost_person.address and found_person.address):
                address_similarity = fuzzy_match(lost_person.address, found_person.address)
                divider+=address_similarity
            if (lost_person.height and found_person.height):
                if(lost_person.height>found_person.height):
                    temp=found_person.height
                    found_person.height=lost_person.height
                    lost_person.height=temp
                height_difference = lost_person.height/found_person.height
                divider+=height_difference
                sum+=1
            if (lost_person.age and found_person.age):
                if(lost_person.age>found_person.age):
                    temp=found_person.age
                    found_person.age=lost_person.age
                    lost_person.age=temp
                age_difference = lost_person.age/found_person.age
                divider+=age_difference
                sum+=1
            print(divider)
            print(sum)
            if(image_similarity>50 and sum<4):
                matches.append((lost_person, found_person))
                continue
            # Consider matches where the attributes have a certain similarity threshold
            if (divider/sum>=0.7):
                        # You have a match, add to matches list
                matches.append((lost_person, found_person))

    return matches



@api_view(['GET'])
def match_items_view(request):
    matches = match_items()  # No need to pass request._request here
    for lost_item, found_item in matches:
        # get_or_create() checks if the entry already exists. If not, it creates a new one.
        _, created = matched_i.objects.get_or_create(lost_id=lost_item, found_id=found_item)

    matches_data = [{'lost_item': lost_item.id, 'found_item': found_item.id} for lost_item, found_item in matches]
    return Response(matches_data)

@api_view(['GET'])
def match_person_view(request):
    matches = match_person()  # No need to pass request._request here
    for lost_person, found_person in matches:
        # get_or_create() checks if the entry already exists. If not, it creates a new one.
        _, created = matched_p.objects.get_or_create(lost_id=lost_person, found_id=found_person)

    matches_data = [{'lost_person': lost_person.id, 'found_person': found_person.id} for lost_person, found_person in matches]
    return Response(matches_data)


@api_view(['GET'])
def update_matched(request):
    matches = match_items()  # No need to pass request._request here
    for lost_item, found_item in matches:
        matched_i.objects.create(lost_id=lost_item,found_id=found_item)
    matches_data = [{'lost_item': lost_item.id, 'found_item': found_item.id} for lost_item, found_item in matches]
    return Response(matches_data)

def detect_face(image_np):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

    # Load the haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the image using OpenCV
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    return faces

def compare_faces(image1_file, image2_file):
    # Load the images using PIL
    image1 = Image.open(image1_file)
    image2 = Image.open(image2_file)

    # Convert the images to numpy array
    image1_np = np.array(image1)
    image2_np = np.array(image2)

    # Detect faces in the images using face_recognition
    face_locations1 = face_recognition.face_locations(image1_np)
    face_locations2 = face_recognition.face_locations(image2_np)

    if len(face_locations1) == 0:
        return "No face found in image 1"

    if len(face_locations2) == 0:
        return "No face found in image 2"

    # Extract face encodings from the images
    face1_encodings = face_recognition.face_encodings(image1_np, face_locations1)
    face2_encodings = face_recognition.face_encodings(image2_np, face_locations2)

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
        return max_similarity
    else:
        return 0

# Compare the images
#result = compare_faces(image1_path, image2_path)

#print(result)
@api_view(['POST'])
def compare_faces_view(request):
    # Get the image files from the request
    im=lost_P.objects.get(id=1)
    im2=lost_P.objects.get(id=2)
    image1_file = im.image_url
    image2_file = im2.image_url

    # Check if both images were provided
    if image1_file is None or image2_file is None:
        return Response("Both images must be provided", status=400)

    # Compare the faces in the images
    compare_result = compare_faces(image1_file, image2_file)

    # Return the result
    return Response(compare_result)
