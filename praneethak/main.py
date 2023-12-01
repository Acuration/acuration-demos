#DID TASK-1
from parse_sitemap import parse_sitemap
from crawl import crawl_url  

def main():
    sitemap_path = r'C:\Users\pkanv\OneDrive\Desktop\Acuration\acuration-demos\myenergi_sitemap.xml'
    output_folder = "output_folder"

    # Parse the local sitemap file to get a list of URLs
    urls = parse_sitemap(sitemap_path)

    if urls:
        # Iterate through each URL and crawl the website
        for url in urls:
            crawl_url(url, output_folder)

        print("Crawling completed.")
    else:
        print(f"Failed to parse sitemap from {sitemap_path}")

if __name__ == "__main__":
    main()
