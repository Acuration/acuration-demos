import requests
import os
import hashlib
from bs4 import BeautifulSoup
import time

pdf_folder_path = r'C:\Users\admin\Desktop\ACURATION FINAL FOLDER\task-2 serp\pdfs'
html_folder_path = r'C:\Users\admin\Desktop\ACURATION FINAL FOLDER\task-2 serp\html_files'

def crawl(url):
    #hashing url for filename
    print('Waiting for 15 secs... (crawl)', end=' ')
    time.sleep(15)
    print('Done waiting.. now crawling')
    pdf_file_name = pdf_folder_path+'\\'+str(hashlib.md5(url.encode()).hexdigest()) + '.pdf'
    html_file_name = html_folder_path+'\\'+str(hashlib.md5(url.encode()).hexdigest()) + '.html'
    if not (os.path.exists(pdf_file_name) and os.path.exists(html_file_name)):
        try:
            print('in try block (crawl)')
            response = requests.get(url)
            print('got response (crawl)')

            if 'application/pdf' in response.headers.get('Content-Type'):
                with open(pdf_file_name, 'wb') as f:
                    f.write(response.content)
                return response.text, 'pdf'
            else:
                with open(html_file_name, 'w', encoding="utf-8") as f:
                    f.write(response.text)

                # for getting text from html
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

                return text, 'html' #return text from html
        except:
            print('There is some error')
            return None, None
    else:
        print('Already exists')
        return None, None
    
    return None, None
    