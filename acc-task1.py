# -*- coding: utf-8 -*-
"""intern_task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vgaQ1ysZgCy_XkMXuYAHVmkysFCFhues
"""

#extracting urls from sitemap
import requests
from bs4 import BeautifulSoup

def parse_sitemap(sitemap_path):
  try:
    #using get req to get data
    f=requests.get(sitemap_path)
    k=f.content
    #using xml parser to find all links
    soup = BeautifulSoup(k, 'xml')
    urls_list = []
    #getting all the links
    loc_tags =soup.find_all('loc')
    #adding all links into a list
    for i in loc_tags:
          urls_list.append(i.get_text())
    return urls_list

  except Exception as e:
        print(f"An error occurred: {e}")
        return None

import re

def clean_html_and_extract_text(html_text):
  try:
    #using a html parser
    soup=BeautifulSoup(html_text,'html.parser')
    # Remove JavaScript code
    for script in soup(['script', 'style']):
        script.extract()

    # get text
    text = soup.get_text()
    text=text.replace("|","")
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    #remove blank lines
    text = '\n'.join(line for line in lines if line)


    return text
  except Exception as e:
      print(f"An error occurred: {e}")
      return None

#to extract content from url
import requests
import time
import urllib.request


def fetch_html_content(url):
  try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    # Add a delay to avoid making too many requests in a short period
    time.sleep(2)  # Sleep for 2 seconds
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as fp:
            # Read the content as bytes
            mybytes = fp.read()

        # Decode the bytes into a string
    data = mybytes.decode("utf-8")

    return data
  except Exception as e:
        print('There was an error in fetching {}: {}'.format(url, e))
        return None

#to save extracted html and text content into file
import os
from os.path import exists
from bs4 import BeautifulSoup

def save_to_file(text,path,name):
  try:

    if not os.path.exists(folder_path):
          os.makedirs(folder_path)
    #check if file already exsists
    if exists(name):
          print('HTML file already exists')
          return


      #fun=open(os.path.join(path,name),"w")
    with open(os.path.join(path,name),"w") as file:
            file.write(str(text))
  except Exception as e:
        print(f'An error occurred while saving to file {name}: {e}')

from urllib.parse import urlparse
from pathlib import Path
from urllib.parse import urlparse, unquote

def generate_file_name(url):
    # Parse URL to get path
    path = urlparse(url).path
    # Remove special characters and decode URL encoding
    filename = unquote("".join([c if c.isalnum() or c in ('_', '-') else '_' for c in path]))
    # Limit filename length to avoid issues
    filename = filename[:255]  # Adjust the limit as needed
    return filename



import requests
import os
from urllib.parse import urlparse
def download_pdf(url,folder_path):
        folder_path+="/pdf_downloads"
        if not os.path.exists(folder_path):
              os.makedirs(folder_path)
        filename=generate_file_name(url)+".pdf"
        if exists(filename):
          print('file already exists')
          return

        response = requests.get(url)
        pdf = open(os.path.join(folder_path,filename), 'wb')
        pdf.write(response.content)
        pdf.close()

from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse


def crawl_url(url, folder_path):
  #to check type of url
  try:
    r = requests.get(url)
    content_type = r.headers.get('content-type')
#pdf file
    if 'application/pdf' in content_type:
      download_pdf(url, folder_path)
#html file
    elif 'application/zip' in content_type:
      return
    else:
        filename = generate_file_name(url)
        if exists(filename):
          print('file already exists')
          return
        # Fetch the website content using requests or another library.
        html_content = fetch_html_content(url)
        soup=BeautifulSoup(html_content,"html.parser")

        # Clean the HTML content using the clean_html function.
        extracted_text = clean_html_and_extract_text(html_content)
        # Store the HTML content and extracted text in separate files within the folder.
        # here filename is the crawled_url_in_underscores

        save_to_file(soup.prettify(), folder_path+"/html_files", f"{filename}.html")
        save_to_file(extracted_text, folder_path+"/text_files", f"{filename}.txt")

    #else:
     # print('Unknown type: {}'.format(content_type))
  except Exception as e:
      print(url,e)

#main function getting sitemap_path
import os
import requests

folder_path="/content/drive/MyDrive/data"
sitemap_path="https://raw.githubusercontent.com/Acuration/acuration-data-store/main/honeywell_sitemap.xml"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


urls_list=parse_sitemap(sitemap_path)

for link in urls_list:
    #cleaning and extracting data
    crawl_url(link,folder_path)