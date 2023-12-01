---
## Task: Sitemap Parsing, URL Crawling, HTML Cleaning, and Text Extraction

### Overview

The goal of this task is to write Python code to parse a sitemap.xml file, crawl each URL listed in the sitemap, clean the HTML content, extract the main text, and store both the HTML and cleaned text in separate files. Finally, the contents of the folder should be uploaded to the specified GitHub repository as a pull request.

### Prerequisites

- Basic knowledge of Python programming.
- Familiarity with Git and GitHub.
- Access to a sitemap.xml file.

### Task Description

1. **Setup:**

   - Clone the GitHub repository to your local machine:
     ```
     git clone https://github.com/Acuration/acuration-demos
     ```

2. **Sitemap Parsing Function:**

   - Write a Python function `parse_sitemap` that takes the path to the sitemap.xml file as an input and returns a list of URLs found in the sitemap.

   ```python
   def parse_sitemap(sitemap_path):
       # Your code here
       return url_list
   ```

3. **HTML Cleaning Function:**

   - Write a Python function `clean_html_and_extract_text` that takes an HTML document as input and performs the following tasks:
     - Remove HTML tags.
     - Remove special characters and extra whitespaces.
     - Normalize the text.
     You can use libraries like BeautifulSoup for HTML parsing.

   ```python
   def clean_html_and_extract_text(html_text):
       # Your code here
       return cleaned_text
   ```

4. **Crawl Function:**

   - Write a Python function `crawl_url` that takes a URL as input, fetches the website content, cleans the HTML, extracts the text, and stores both the HTML and cleaned text in separate files within a designated folder.

   ```python
   def crawl_url(url, folder_path):
       # Fetch the website content using requests or another library.
       html_content = fetch_html_content(url)

       # Clean the HTML content using the clean_html function.
       extracted_text = clean_html_and_extract_text(html_content)

       # Store the HTML content and extracted text in separate files within the folder.
       # here filename is the crawled_url_in_underscores
       save_to_file(html_content, folder_path, "<filename>_html.html")
       save_to_file(extracted_text, folder_path, "<filename>_extracted_text.txt")
   ```

5. **Main Script:**

   - Create a Python script that utilizes the `parse_sitemap` and `crawl_url` functions to iterate through the URLs in the sitemap, crawl each website, and store the contents.

6. **GitHub Repository Contribution:**

   - Commit and push the cleaned HTML and extracted text files, along with the original HTML files, to the GitHub repository as a new branch.

### Submission

- Ensure your code is well-documented, and any necessary instructions for running the script are included in a README file.
- Submit your pull request to the main repository.

### Evaluation

You will be evaluated based on the following criteria:

- Successful parsing of the sitemap.xml file.
- Correct crawling of website URLs and storing both HTML and extracted text.
- Effective HTML cleaning, resulting in clean and normalized text.
- Accurate extraction of the main content from HTML pages.
- Proper organization and naming of files within the folder structure.
- Committing and pushing cleaned HTML and text files to GitHub with clear documentation.

### Additional Resources

- [Python Requests Library Documentation](https://docs.python-requests.org/en/master/)
- [Git and GitHub Guide](https://guides.github.com/)

Good luck, and feel free to reach out if you have any questions or need assistance during the task!
