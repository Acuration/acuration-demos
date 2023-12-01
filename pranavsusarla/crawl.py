#import the clean_html_and_extract text from clean.py
from clean import clean_html_and_extract_text

def crawl_url(url, folder_path):
    #import requests library
    import requests
    #import os.path for checking if a file already exists
    from os.path import exists

    #trying to fetch the url using requests
    try:
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

        #creating the file name for the html file
        ht_name = '{fp}/{ur}'.format(fp=folder_path, ur=url)[:200] + '_html.html'

        #checking if the file already exists
        if exists(ht_name): 
            return
        else: 
            ht = open(ht_name, 'w', encoding="utf-8")
            ht.write(html_content)
            ht.close()

        #creating the file name for the text file
        clean_ht_name = '{fp}/{ur}'.format(fp=folder_path, ur=url)[:200] + '_extracted_text.txt'

        #checking if the file already exists
        if exists(clean_ht_name): 
            return
        else: 
            clean_ht = open(clean_ht_name, 'w', encoding="utf-8")
            clean_ht.write(extracted_text)
            clean_ht.close()
    
    #if there are any errors
    except Exception as e:
        print('There was an error in fetching {}: {}'.format(url, e))