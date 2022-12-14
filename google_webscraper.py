"""
Title: google_webscraper.py
Developer: Kevin Wu
Description: Webscraper for general Google searches.
"""

import requests
from bs4 import BeautifulSoup
from googlesearch import search
import twitter_api_module

"""
Global variables (used as static)
"""
wiki = ["w", "wiki", "wikipedia"]
google = ["g", "google"]

"""
Check if the specified website is valid.

@param website is the website to verify
@return a valid website
"""
def verify_website(website):
    while (website.lower() not in wiki) and (website.lower() not in google):
        print("Invalid website.")
        website = input("Search in [ Google | Wikipedia ]: ")
    return website

"""
Check if search terms are valid.

@param website is the website choice
@param search_terms are the search terms to verify
@return valid search terms
"""
def verify_search_terms(website, search_terms):
    if website in google:
        while search_terms.isspace():
            print("Invalid search. Search is empty.")
            search_terms = input("Enter search term: ")
        return search_terms
    elif website in wiki:
        while search_terms.isspace():
            print("Invalid search. Search is empty or contains spaces.")
            search_terms = input("Enter search term: ")
        search_terms = search_terms.replace(' ', '_')
        return search_terms

"""
Query user for search terms and website.

@return search terms and the website to search in
"""
def specify_search_parameters():
    website = input("Search in [ Google | Wikipedia ]: ")
    website = verify_website(website)

    search_terms = input("Enter search term: ")
    search_terms = verify_search_terms(website, search_terms)

    # Ask if user wants to filter their search, then take in search terms or leave parse_search empty
    parse_search = " "
    while parse_search.lower() != "y" and parse_search.lower() != "n":
        parse_search = input("Filter search for sentence with keywords [ Y | N ]: ")
    if parse_search.lower() == "y":
        parse_search = " "
        while parse_search.isspace():
            parse_search = input("Enter search terms: ")
    elif parse_search.lower() == "n":
        parse_search = " "
    return search_terms, website, parse_search

"""
Save search output to temp_log.txt file.

@param output is the output text
"""
def save_to_file(output):
    file = open("temp_log.txt", "w+", encoding="utf-8")
    for sentence in output:
        file.write(sentence + "\n")
    file.close()

"""
Filter the search to sentences which contain the search terms and print them out.

@param search_terms are the terms to search for
@param website_elements is the website data
@return the text output of the page
"""
def filter_search(parse_search, website_elements):
    text_output = []
    term_list = parse_search.split(' ')
    for i in range(len(term_list)):
        term_list[i] = term_list[i].lower()
    for data in website_elements.find_all("p"):
        contains_term = False
        text = data.get_text()
        text = text.split(' ')
        for word in text:
            if word.lower() in term_list:
                contains_term = True
                break
        if contains_term:
            text = data.get_text()
            print(text)
            text_output.append(text)
    return text_output

"""
Examine if URL is a tweet.

@param url is the URL to verify
@return the tweet_id if the URL is a tweet, -1 otherwise
"""
def is_tweet(url):
    tweet_id = twitter_api_module.validate_link(url)
    return tweet_id

"""
Search google for the top 10 results of the search terms and print them out.

@param search_terms are the terms to search
@param parse_search is whether to filter the search 
"""
def search_google(search_terms, parse_search):
    output = []
    for url in search(search_terms, tld="co.in", num=10, stop=10, pause=2):
        print(url)
        output.append(url)
        tweet_id = is_tweet(url)
        if tweet_id == -1:
            html = requests.get(url)
            website_elements = BeautifulSoup(html.content, 'html.parser')
            if parse_search.isspace():
                for data in website_elements.find_all("p"):
                    text = data.get_text()
                    print(text)
                    output.append(text)
            else:
                text_output = filter_search(parse_search, website_elements)
                for sentence in text_output:
                    output.append(sentence)
        else:
            text = twitter_api_module.return_text(url)
            print(text)
            output.append(text)
        output.append("\n")
    save_to_file(output)

"""
Search the wiki for the search term.

@param search_terms are the terms to search for
@param parse_search is whether to filter the search
"""
def search_wiki(search_terms, parse_search):
    output = []
    url = "https://en.wikipedia.org/wiki/" + search_terms
    html = requests.get(url)
    website_elements = BeautifulSoup(html.content, 'html.parser')
    if parse_search.isspace():
        for data in website_elements.find_all("p"):
            text = data.get_text
            print(text)
            output.append(text)
    else:
        text_output = filter_search(parse_search, website_elements)
        for sentence in text_output:
            output.append(sentence)
    save_to_file(output)

"""
Main function.
"""
def main():
    search_terms, website, parse_search = specify_search_parameters()
    if website in google:
        search_google(search_terms, parse_search)
    elif website in wiki:
        search_wiki(search_terms, parse_search)

"""
Main function guard.
"""
if __name__ == "__main__":
    main()

