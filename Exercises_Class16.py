import requests
import random

BASE_URL = 'https://dog.ceo/api'

def list_breeds():
    response = requests.get(f'{BASE_URL}/breeds/list/all')
    if response.status_code == 200:
        data = response.json()
        breeds = data['message'].keys()
        for breed in breeds:
            print(breed)
    else:
        print('Error occurred while fetching breeds.')

def get_random_image():
    response = requests.get(f'{BASE_URL}/breeds/image/random')
    if response.status_code == 200:
        data = response.json()
        image_url = data['message']
        download_image(image_url)
    else:
        print('Error occurred while fetching the random image.')

def get_random_image_by_breed(breed):
    response = requests.get(f'{BASE_URL}/breed/{breed}/images/random')
    if response.status_code == 200:
        data = response.json()
        image_url = data['message']
        download_image(image_url)
    else:
        print('Error occurred while fetching the random image for the breed.')

def list_sub_breeds(breed):
    response = requests.get(f'{BASE_URL}/breed/{breed}/list')
    if response.status_code == 200:
        data = response.json()
        sub_breeds = data['message']
        if sub_breeds:
            for sub_breed in sub_breeds:
                print(f'{sub_breed} {breed}')
        else:
            print(f'{breed} does not have any sub-breeds.')
    else:
        print('Error occurred while fetching sub-breeds.')

def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open('dog_image.jpg', 'wb') as file:
            file.write(response.content)
        print('Image downloaded successfully.')
    else:
        print('Error occurred while downloading the image.')

print("1. List available breeds")
print("2. Download a random image from all breeds")
print("3. Choose a breed and download a random image")
print("4. List sub-breeds of a breed")

choice = input("Enter your choice (1-4): ")

if choice == '1':
    list_breeds()
elif choice == '2':
    get_random_image()
elif choice == '3':
    breed = input("Enter a breed: ")
    get_random_image_by_breed(breed)
elif choice == '4':
    breed = input("Enter a breed: ")
    list_sub_breeds(breed)
else:
    print("Invalid choice.")