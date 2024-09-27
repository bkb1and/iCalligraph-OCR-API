#利用python的requests库来调用验证api
import requests

def test_ocr_api(image_path):
    url = 'https://8d67-124-160-64-91.ngrok-free.app/ocr'
    
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        
        response = requests.post(url, files=files)
    
    if response.status_code == 200:
        result = response.json()
        print(result['text'])
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        print(response.text)

image_path = '../img/2.png'
test_ocr_api(image_path)