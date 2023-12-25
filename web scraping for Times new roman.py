import requests
from bs4 import BeautifulSoup
import tkinter as tk
def scrape_tnr_headline():
    try:
         # Retrieve and parse data from timesnewroman.ro
         TNRsource = requests.get('https://www.timesnewroman.ro/', headers=headers, timeout=10).text
         soup = BeautifulSoup(TNRsource, 'html.parser')
 
         big_article = soup.find('article')
         big_article_link = big_article.find('a', class_='article-meta')
         big_article_link_string = str(big_article_link)
         string_in_link = big_article_link_string.split('"')
 
         result_label.config(text=string_in_link[3])
    except requests.exceptions.RequestException as e:
         result_label.config(text=f"Error: {e}")
 
# Set up headers for web scraping
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 
# Create the main Tkinter window
root = tk.Tk()
root.title("Web Scraping with Tkinter")
 
# Create a button to trigger web scraping
scrape_button = tk.Button(root, text="Scrape TNR Headline", command=scrape_tnr_headline)
scrape_button.pack(pady=10)
 
# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
