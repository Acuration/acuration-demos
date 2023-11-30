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