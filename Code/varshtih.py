import xml.etree.ElementTree as ET

def parse_sitemap(sitemap_path):
  #parsing
  tree = ET.parse(sitemap_path)
  root = tree.getroot()
  # Define the XML namespace
  ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
  # Find all URL elements in the sitemap
  url_elements = root.findall('.//ns:url/ns:loc', namespaces=ns)
  # Extract URLs from the elements
  url_list = [url_element.text for url_element in url_elements]
  return url_list
sitemap_path='resgroup__sitemap.xml'

from bs4 import BeautifulSoup
import re
def clean_html_and_extract_text(html_text):
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_text, 'lxml')
    # Extract text content
    text_content = soup.get_text(separator=' ')
    # Remove special characters and extra whitespaces
    cleaned_text = re.sub(r'\s+', ' ', text_content).strip()
    return cleaned_text
html_text = """
# <html>
#   <body>
#     <p>This is an example <b>HTML</b> document.</p>
#     <p>It contains <a href="#">links</a>, <em>emphasis</em>, and other <strong>markup</strong>.</p>
#   </body>
# </html>
"""
clean_html_and_extract_text(html_text)
import requests
import os
from urllib.parse import urlparse
def fetch_html_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # Use the requests library to fetch the HTML content from the URL
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        # Handle the case when the request was not successful
        print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
        return None
def save_to_file(content, folder_path, filename):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, filename)
    # Write the content to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
def crawl_url(url, folder_path):
    # Fetch the website content using requests
    html_content = fetch_html_content(url)
    if html_content is not None:
        # Clean the HTML content using the clean_html_and_extract_text function
        extracted_text = clean_html_and_extract_text(html_content)
        # Generate a filename based on the crawled URL with underscores
        parsed_url = urlparse(url)
        filename = "crawled_" + parsed_url.netloc + parsed_url.path.replace("/", "_") + "_"
        # Store the HTML content and extracted text in separate files within the folder
        save_to_file(html_content, folder_path, filename + "_html.html")
        save_to_file(extracted_text, folder_path, filename + "_extracted_text.txt")
def main():
    sitemap_path='resgroup__sitemap.xml'
    urls = parse_sitemap(sitemap_path)
    for url in urls:
        folder_to_store="storage"
        crawl_url(url, folder_to_store)
main()