import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve

def download_images(url, folder_path):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        
        for img_tag in img_tags:
            img_url = urljoin(url, img_tag.get('src'))
            img_name = os.path.basename(img_url)
            img_path = os.path.join(folder_path, img_name)
            
            try:
                urlretrieve(img_url, img_path)
                print(f"Downloaded: {img_name}")
            except Exception as e:
                print(f"Error downloading {img_name}: {e}")

def main():
    url = input("Enter the URL to download images from: ")
    folder_path = input("Enter the folder path to save images: ")
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    download_images(url, folder_path)
    print("Image download completed.")

if __name__ == "__main__":
    main()