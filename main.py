# I want to make a program to list all website urls in a text file
# So user will input domain and keyword, and the program will merge them and search for the urls
# For example, user inputs "drive.google.com" and "contact", the program will search for "site:drive.google.com contact"
# Then the program will list all urls in the text file
# It will use bing and google search engines

import random
import datetime
import requests
from bs4 import BeautifulSoup

def generate_file_name():
  # Since we don't want to overwrite the file, we will generate a new file name
  # File name will be urls-{date}-{random}.txt
  # Date format will be YYYY-MM-DD
  # Random will be 4 digits
  # Example: urls-20210826-1234.txt

  date = datetime.datetime.now().strftime("%Y%m%d")
  random_number = random.randint(1000, 9999)
  file_name = "urls-" + date + "-" + str(random_number) + ".txt"

  return file_name

def check_duplicate_urls(urls):
  new_urls = []

  for url in urls:
    if url in new_urls:
      continue
    new_urls.append(url)

  return new_urls

def random_user_agent():
  user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Linux; Android 11; SM-G980F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4a Build/RQ1A.201205.008; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/301.0.0.37.477;]",
  ]

  return user_agents[random.randint(0, len(user_agents) - 1)]

def is_url_valid(domain, url):
  if not url.startswith("http") or not url.startswith("https"):
    return False

  # If the url not contains of domain, it's not valid
  if domain not in url:
    return False

  return True

def generate_query(domain, keyword):
  query = "site:" + domain + " " + keyword
  return query

def get_urls_from_bing(domain, keyword):
  urls = []
  search = generate_query(domain, keyword)
  search = "https://www.bing.com/search?q=" + search
  response = requests.get(search, headers={
    "User-Agent": random_user_agent()
  })

  # Bing will block the request if the user agent is not valid
  # So we need to check if the response is valid
  if response.status_code != 200:
    return urls

  # Check if we are not blocked by bing
  if "Please enable cookies." in response.text:
    return urls

  soup = BeautifulSoup(response.text, "html.parser")

  for a in soup.find_all("a", href=True):
    print(a)
    if a["href"].startswith("http"):
      if is_url_valid(domain, a["href"]):
        urls.append(a["href"])

  return urls

def get_urls_from_google(domain, keyword):
  urls = []
  search = generate_query(domain, keyword)
  search = "https://www.google.com/search?q=" + search
  response = requests.get(search, headers={
    "User-Agent": random_user_agent()
  })

  # Google will block the request if the user agent is not valid
  # So we need to check if the response is valid
  if response.status_code != 200:
    return urls

  # Check if we are not blocked by google
  if "Our systems have detected unusual traffic from your computer network" in response.text:
    return urls

  soup = BeautifulSoup(response.text, "html.parser")

  for a in soup.find_all("a", href=True):
    if a["href"].startswith("http"):
      if is_url_valid(domain, a["href"]):
        urls.append(a["href"])

  return urls

def get_urls(domain, keyword):
  urls = []

  [urls.append(url) for url in get_urls_from_bing(domain, keyword)]
  [urls.append(url) for url in get_urls_from_google(domain, keyword)]

  urls = check_duplicate_urls(urls)
  return urls

def main():
  print("Website domain and keyword finder")
  print("This program will list all website urls in a text file")
  print("You will input domain and keyword, and the program will merge them and search for the urls")
  print("For example, you input 'drive.google.com' and 'contact', the program will search for 'site:drive.google.com contact'")
  print("Then the program will list all urls in the text file")
  print("=====================================")
  domain = input("Enter domain: ")
  keyword = input("Enter keyword: ")
  print("=====================================")
  print("Searching for urls...")

  urls = get_urls(domain, keyword)
  file_name = generate_file_name()

  with open(file_name, "w") as f:
    for url in urls:
      f.write(url + "\n")

  print("=====================================")
  print("Urls are saved in " + file_name)
  print("=====================================")

if __name__ == "__main__":
  main()