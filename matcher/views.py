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
@api_view(['GET'])
def health_check(request):
    response =send_images_for_comparison('/home/par/Desktop/finder/mediafiles/images/Dv.jpg', '/home/par/Desktop/finder/mediafiles/images/Dv.jpg')
    return JsonResponse(response)
@api_view(['POST'])
def compare_images(request):
    image1 = request.FILES.get('image1')
    image2 = request.FILES.get('image2')

    if not image1 or not image2:
        return JsonResponse({'error': 'Please provide both image1 and image2 files.'}, status=400)
    
    image1_data = face_recognition.load_image_file(image1)
    image2_data = face_recognition.load_image_file(image2)
    
    face_encodings1 = face_recognition.face_encodings(image1_data)
    face_encodings2 = face_recognition.face_encodings(image2_data)
    
    if len(face_encodings1) == 0 or len(face_encodings2) == 0:
        return JsonResponse({'error': 'No faces found in one or both images.'}, status=400)
    
    face_distance = face_recognition.face_distance(face_encodings1, face_encodings2)
    similarity = 1 - face_distance
    
    response = {
        'similarity': float(similarity[0]) * 100
    }
    
    return JsonResponse(response)

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
            detail_similarity = fuzzy_match(lost_item.detail, found_item.detail)
            serial_similarity = fuzzy_match(lost_item.serial_n, found_item.serial_n)
            address_similarity = fuzzy_match(lost_item.adress, found_item.adress)
            city_similarity = fuzzy_match(lost_item.city, found_item.city)
            count=(detail_similarity+serial_similarity+address_similarity+city_similarity)/4
            
            # Consider matches where the details, serial number, and address are 80% similar
            if count >= 0.7:
                if lost_item.lost_date and found_item.lost_date:
                    # Consider matches where the found_date is within 30 days of the lost_date
                    date_difference = abs((found_item.lost_date - lost_item.lost_date).days)
                    if date_difference <= 30:
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
            
            # Consider matches where the attributes have a certain similarity threshold
            if (divider/sum>=0.7):
                        # You have a match, add to matches list
                matches.append((lost_person, found_person))

    return matches



@api_view(['GET'])
def match_items_view(request):
    matches = match_items()  # No need to pass request._request here
    for lost_item, found_item in matches:
        matched_i.objects.create(lost_id=lost_item,found_id=found_item)
    matches_data = [{'lost_item': lost_item.id, 'found_item': found_item.id} for lost_item, found_item in matches]
    return Response(matches_data)

@api_view(['GET'])
def match_person_view(request):
    matches = match_person()  # No need to pass request._request here
    for lost_person, found_person in matches:
        matched_i.objects.create(lost_id=lost_person,found_id=found_person)
    matches_data = [{'lost_item': lost_item.id, 'found_item': found_item.id} for lost_item, found_item in matches]
    return Response(matches_data)


@api_view(['GET'])
def update_matched(request):
    matches = match_items()  # No need to pass request._request here
    for lost_item, found_item in matches:
        matched_i.objects.create(lost_id=lost_item,found_id=found_item)
    matches_data = [{'lost_item': lost_item.id, 'found_item': found_item.id} for lost_item, found_item in matches]
    return Response(matches_data)

