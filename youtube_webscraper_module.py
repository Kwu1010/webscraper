"""
Title: youtube_webscraper_module.py
Developer: Kevin Wu
Description: Webscraper module for Youtube.
"""

import requests
from bs4 import BeautifulSoup

"""
Validate that the given link is for Youtube.

@param url is the URL to check
@return True if valid, False otherwise
"""
def validate_link(url):
    url_split = url.split('/')
    if "www.youtube.com" in url_split:
        return True
    else:
        return False

"""
Return the text from a Youtube link.

@param url is the URL to open
@return the information about the Youtube video
"""
def extract_info(url):
    print(url)
    html = requests.get(url)
    website_elements = BeautifulSoup(html.content, 'html.parser')
    for data in website_elements.find_all("title"):
        print(data.get_text())

"""
Main function. Takes a bearer token and url to extract text from a tweet.
"""
def main():
    url = "https://www.youtube.com/watch?v=OZEQiP2rySQ"
    extract_info(url)

"""
Main function guard.
"""
if __name__ == "__main__":
    main()