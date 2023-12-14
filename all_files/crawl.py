import requests
import os
import hashlib

def crawl(url, folder_path, extension):
    response = requests.get(url)

    #hashing url for filename
    file_name = folder_path+'\\'+str(hashlib.md5(url.encode()).hexdigest()) + extension

    if not os.path.exists(file_name):
        if extension == '.pdf':
            with open(file_name, 'wb') as f:
                f.write(response.content)
        elif extension == '.html':
            print(r.content)