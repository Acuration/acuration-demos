#import the clean_html_and_extract text from clean.py
from clean import clean_html_and_extract_text

#import modify_url to replace all the special characters in the url with _
from modify_url import modify_url

# for correcting the folder path
from modify_folder_path import modify_folder_path

def crawl_url(url, folder_path):
    #import requests library
    import requests

    #import os.path for checking if a file already exists
    from os.path import exists

    #replacing special chars with _ in url
    mod_url = modify_url(url)

    #correcting the folder_path
    mod_folder_path = modify_folder_path(folder_path)

    #creating the file name for the html file
    html_filename = '{fp}/{ur}'.format(fp=mod_folder_path, ur=mod_url)[:200] + '_html.html'

    #creating the file name for the text file
    clean_html_text_filename = '{fp}/{ur}'.format(fp=mod_folder_path, ur=mod_url)[:200] + '_extracted_text.txt'

    #checking if html files with this filename exist
    if exists(html_filename): 
        return
    
    #checking if text files with this filename exist
    if exists(clean_html_text_filename):
        return

    #trying to fetch the url using requests
    try:
        r = requests.get(url)

        #checking if its not a html file
        content_type = r.headers.get('content-type')
        if 'text/html' not in content_type:
            #skip for now if url does not have html content
            return

        html_content = r.text
        extracted_text = clean_html_and_extract_text(html_content)

        #creating the html file
        ht = open(html_filename, 'w', encoding="utf-8")
        ht.write(html_content)
        ht.close()

        #creating the text file 
        clean_ht = open(clean_html_text_filename, 'w', encoding="utf-8")
        clean_ht.write(extracted_text)
        clean_ht.close()
    
    #if there are any errors
    except Exception as e:
        print('There was an error in fetching {}: {}'.format(url, e))