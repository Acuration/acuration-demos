def modify_url(url):
    #special characters
    special_characters = ['#','%','&','{','}','\\','<','>','*','?','/',' ','$','!',"'",'"',':','@','+','`','|','=','.',',','~','^','(',')',';']
        
    #replacing special characters with _
    for c in url:
        if c in special_characters:
            url = url.replace(c, '_')
    
    return url