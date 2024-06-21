# -*- coding: utf-8 -*-
# @Time    : 2024/4/1 22:00
# @Author  : yingzhu
# @FileName: download_paper.py

import os
import re
import time
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def get_paper_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h1', class_='title mathjax').get_text()
    title = title.replace('Title:', '').strip()  # Removing 'Title:' prefix

    # Cleaning and formatting the title for use in filenames
    title = re.sub('[^a-zA-Z0-9 \n\.]', '', title)  # Remove invalid characters
    title = re.sub(' +', ' ', title).strip()  # Remove extra spaces
    title = title[:50]  # Limit title length if necessary
    return title


def download_pdfs(url_list, destination_folder, delay=5):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created directory: {destination_folder}")

    downloaded_files = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    for url in url_list:
        try:
            paper_title = get_paper_title(url)
            parsed_url = urlparse(url)
            file_name = parsed_url.path.split('/')[-1] + f"_{paper_title}.pdf"
            file_path = os.path.join(destination_folder, file_name)
            pdf_url = url.replace("/abs/", "/pdf/") + ".pdf"

            print(f"Downloading {pdf_url}...")

            response = requests.get(pdf_url, headers=headers)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                downloaded_files.append(file_path)
                print(f"Downloaded and saved to {file_path}")
            else:
                print(f"Failed to download PDF from {url}. Status Code: {response.status_code}")

        except Exception as e:
            print(f"An error occurred while downloading {url}: {e}")

        time.sleep(delay)

    return downloaded_files


def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]


if __name__ == '__main__':
    print("------------------ start ------------------")

    file_path = r"D:\code2\python-code\artificial-intelligence\paper.txt"
    url_list = read_urls_from_file(file_path)

    destination_folder = r"crawl\papers"
    downloaded_files = download_pdfs(url_list, destination_folder)
    print("Downloaded files:", downloaded_files)

    print("------------------ end ------------------")

    """
    https://arxiv.org/abs/1904.11486
    https://arxiv.org/abs/1811.11168
    """
