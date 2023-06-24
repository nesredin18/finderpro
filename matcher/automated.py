import requests
def send_images_for_comparison(image1_path, image2_path):
    url = 'http://127.0.0.1:8000/matcher/'  # Replace with the actual URL of the destination DRF system's image comparison endpoint
    
    files = {
        'image1': open(image1_path, 'rb'),
        'image2': open(image2_path, 'rb')
    }

    response = requests.post(url, files=files)
    print(response.content)
    result = response.json()
    
    # Handle the result as per your requirements
    if response.status_code == 200:
        similarity = result['similarity']
        print(f"The similarity between the images is: {similarity}%")
    else:
        error = result.get('error', 'Unknown error')
        print(f"An error occurred: {error}")

# Usage example:

