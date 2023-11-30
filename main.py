def parse_sitemap(sitemap_path):
    #importing the relevant function for extracting data from an xml file
    import xml.etree.ElementTree as ET 
    
    #getting the whole file as a tree
    tree = ET.parse(sitemap_path)
    
    #getting the root element
    root = tree.getroot()

    #initializing the url_list
    url_list = []

    #iterating over the root element and extracting the urls
    for url in root:
        for t in url:
            if t.tag == '{http://www.sitemaps.org/schemas/sitemap/0.9}loc':
                url_list.append(t.text)
    
    #returning the list of urls
    return url_list

def clean_html_and_extract_text(html_content):
    #import beautifulsoup4 library for parsing html files
    from bs4 import BeautifulSoup

    #creating a BeatifulSoup object: soup
    soup = BeautifulSoup(html_content, "html.parser")
    
    #storing the text in ans variable
    ans = soup.get_text().strip()

    #returning ans
    return ans

def crawl_url(url, folder_path):
    #import requests library
    import requests

    r = requests.get(url)

    #checking if its a pdf
    content_type = r.headers.get('content-type')
    if 'text/html' not in content_type:
        #skip for now if url does not have html content
        return

    html_content = r.text
    extracted_text = clean_html_and_extract_text(html_content)

    special_characters = ['#','%','&','{','}','\\','<','>','*','?','/',' ','$','!',"'",'"',':','@','+','`','|','=','.',',','~','^','(',')',';']
    
    #replacing special characters with _
    for c in url:
        if c in special_characters:
            url = url.replace(c, '_')
    
    #correcting the folder_path
    for c in folder_path:
        if c == '\\':
            folder_path = folder_path.replace('\\', '/')

    #creating and storing the html files
    ht_name = '{fp}/{ur}'.format(fp=folder_path, ur=url)[:200] + '_html.html'
    ht = open(ht_name, 'w', encoding="utf-8")
    ht.write(html_content)
    ht.close()

    #saving extracted text files
    clean_ht_name = '{fp}/{ur}'.format(fp=folder_path, ur=url)[:200] + '_extracted_text.txt'
    clean_ht = open(clean_ht_name, 'w', encoding="utf-8")
    clean_ht.write(extracted_text)
    clean_ht.close()

sitemap_path = r'C:\Users\admin\Codes\acuration\first_task\suzlon_sitemap.xml'

#getting all urls
list_of_all_urls = parse_sitemap(sitemap_path)

for i in range(len(list_of_all_urls)):
    crawl_url(list_of_all_urls[i], r'C:\Users\admin\Codes\acuration\first_task\files2')
    print(list_of_all_urls[i])
    print(i)
