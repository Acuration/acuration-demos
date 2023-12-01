from parse_sitemap import parse_sitemap
from clean import clean_html_and_extract_text
import os
import requests
import re

def fetch_html_content(url):
    # Simulate fetching HTML content, replace this with actual code using requests or another library.
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def crawl_url(url, output_folder):
    # Fetch the website content using requests or another library.
    html_content = fetch_html_content(url)

    if html_content is not None:
        # Clean the HTML content using the clean_html_and_extract_text function.
        cleaned_text = clean_html_and_extract_text(html_content)

        # Derive filename from the URL with underscores
        filename = re.sub(r'\W+', '_', url)

        # Ensure the output folder exists or create it
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Write original HTML to a file
        html_file_path = os.path.join(output_folder, f"{filename}_html.html")
        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        # Write cleaned text to a file
        text_file_path = os.path.join(output_folder, f"{filename}_extracted_text.txt")
        with open(text_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(cleaned_text)

        print(f"Files saved successfully in {output_folder}")
    else:
        print(f"Failed to fetch content from {url}")

