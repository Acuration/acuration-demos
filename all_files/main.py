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

