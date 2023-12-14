import requests
import os
import hashlib
from bs4 import BeautifulSoup

def crawl(url, folder_path, extension):
    try:
        response = requests.get(url)

        #hashing url for filename
        file_name = folder_path+'\\'+str(hashlib.md5(url.encode()).hexdigest()) + extension

        if not os.path.exists(file_name):
            if extension == '.pdf':
                with open(file_name, 'wb') as f:
                    f.write(response.content)
            elif extension == '.html':
                # writing .html files into html_files folder
                with open(file_name, 'w', encoding="utf-8") as f:
                    f.write(response.text)

                # for getting text from html and writing into the text_files folder
                soup = BeautifulSoup(response.text, "html.parser")

                #got below code from stackoverflow
                for script in soup(["script", "style"]):
                    script.decompose()

                text = soup.get_text()

                # break into lines and remove leading and trailing space on each
                lines = (line.strip() for line in text.splitlines())
                # break multi-headlines into a line each
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                # drop blank lines
                text = '\n'.join(chunk for chunk in chunks if chunk)

                file_name = folder_path+'\\extracted_html_text_files\\'+str(hashlib.md5(url.encode()).hexdigest()) + '.txt'

                with open(file_name, 'w', encoding="utf-8") as f:
                    f.write(text)
    except:
        print('There is some error')
