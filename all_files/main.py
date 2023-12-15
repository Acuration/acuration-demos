from crawl import crawl
from parse_xml import parse_sitemap

sitemap_path = r'C:\Users\admin\Desktop\VNR\Acuration\acuration-demos-1\all_files\suzlon_sitemap.xml'

url_list = set(parse_sitemap(sitemap_path=sitemap_path))

#segregating the types of urls
pdf = []
mp3 = []
html = []
php = []

for url in url_list:
    if url[-4:] == '.pdf':
        pdf.append(url)
    elif url[-4:] == '.php':
        php.append(url)
    elif url[-4:] == '.mp3':
        mp3.append(url)
    else:
        html.append(url)

folder_path_pdf = r'C:\Users\admin\Desktop\VNR\Acuration\acuration-demos-1\all_files\pdf_files'
folder_path_html = r'C:\Users\admin\Desktop\VNR\Acuration\acuration-demos-1\all_files\html_files'

# # crawling html urls
for i in range(len(html)):
    crawl(html[i], folder_path_html, '.html')
    print('({}/{}) crawled'.format(i, len(html)))

# # crawling pdf urls and downloading pdfs
for i in range(len(pdf)):
    crawl(pdf[i], folder_path_pdf, '.pdf')
    print('({}/{}) pdfs crawled'.format(i+1, len(pdf)))