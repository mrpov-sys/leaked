import requests
from bs4 import BeautifulSoup
import os

def download_file(url, directory):
    response = requests.get(url, stream=True)
    file_name = url.split("/")[-1]
    file_path = os.path.join(directory, file_name)
    with open(file_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

def download_all_files(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a")
    directory = os.path.basename(url)
    if not os.path.exists(directory):
        os.makedirs(directory)
    for link in links:
        href = link.get("href")
        if href and not href.startswith("#"):
            if href.startswith("http"):
                download_file(href, directory)
            else:
                download_file(url + href, directory)

url = ("Masukan Url Target") 
download_all_files(url)