from parse import parse_sitemap
from crawl import crawl_url

sitemap_path = r'C:\Users\admin\Codes\acuration\first_task\suzlon_sitemap.xml'

#getting all urls
list_of_all_urls = parse_sitemap(sitemap_path)

for i in range(len(list_of_all_urls)):
    crawl_url(list_of_all_urls[i], r'C:\Users\admin\Codes\acuration\first_task\files2')
    print(list_of_all_urls[i])
    print(i)
