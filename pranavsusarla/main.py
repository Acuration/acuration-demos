#importing all the function
from parse import parse_sitemap
from crawl import crawl_url

sitemap_path = r'C:\Users\admin\Codes\acuration\first_task\suzlon_sitemap.xml'

#getting all urls
list_of_all_urls = parse_sitemap(sitemap_path)

# import requests
# for i in range(260, 266):
#     print(list_of_all_urls[i])
#     # print(requests.get(list_of_all_urls[i]).text)

# print(len(list_of_all_urls))
# print(list_of_all_urls[4016])

# crawl_url(list_of_all_urls[4018],r'C:\Users\admin\Codes\acuration\first_task\files2')
#saving html and text files into a folder named files
# c = 0 
# for url in list_of_all_urls:
#     crawl_url(url, r'C:\Users\admin\Codes\acuration\first_task\files2')
#     print(url)
#     print(c)
#     c += 1

for i in range(4015, len(list_of_all_urls)):
    crawl_url(list_of_all_urls[i], r'C:\Users\admin\Codes\acuration\first_task\files2')
    print(list_of_all_urls[i])
    print(i)
