import requests
import utils.debug as debug
from bs4 import BeautifulSoup
import utils.check_url as check
from config.url import URLConfig
from utils.generate_agent import generate_user_agent

def generate_query(domain, keyword, search_engine="google"):
  if search_engine == "bing":
    return f"sites:{domain} {keyword}"

  return f"site:{domain} {keyword}"

def bypass_safe_search(url):
  # This function is used to bypass the safe search
  # If the search engine is google, we need to add &safe=off to the url
  if "google" in url:
    return f"{url}&safe=off"
  elif "bing" in url:
    return f"{url}&SafeSearch=off"

  return url

def get_data_from_search_engine(domain, keyword):
  # First, we need to get the search engine url from the config
  # If the search engine is not available, we will return empty list
  # This is to prevent the program from crashing
  # If search engine more than 1, we will loop through all of them
  urls = []
  blocked = False

  for search_engine in URLConfig['search_engine_url']:
    blocked = False

    query = generate_query(domain, keyword).replace(" ", "+")
    response = requests.get(bypass_safe_search(search_engine + query), headers={
      "User-Agent": generate_user_agent()
    })

    if response.status_code != 200:
      debug.log(f"Failed to get data from search engine: {search_engine}")
      continue

    for block in URLConfig['blocked_text']:
      if block in response.text:
        debug.log(f"Blocked by search engine: {search_engine}")
        blocked = True
        break

    if blocked:
      continue

    soup = BeautifulSoup(response.text, "html.parser")

    for a in soup.find_all("a", href=True):
      if not check.is_url_valid(domain, a["href"]):
        continue
      urls.append(a["href"])

  filtered_urls = check.check_duplicate_urls(urls)
  debug.log(f"Gathered {len(filtered_urls)} urls from search engine for keyword: {keyword}")

  return filtered_urls
