def clean_html_and_extract_text(html_content):
    #import beautifulsoup4 library for parsing html files
    from bs4 import BeautifulSoup

    #creating a BeatifulSoup object: soup
    soup = BeautifulSoup(html_content, "html.parser")
    
    #storing the text in ans variable
    ans = soup.get_text().strip()

    #returning ans
    return ans