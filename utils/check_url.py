import utils.debug as debug
from config.url import URLConfig

def check_duplicate_urls(urls):
  new_urls = []

  if not urls or len(urls) == 0:
    debug.log("Data urls is empty, nothing to check, skipping process")
    return new_urls

  for url in urls:
    if url in new_urls:
      continue
    new_urls.append(url)

  debug.log(f"Duplicate urls has been removed, total urls: {len(new_urls)}, from {len(urls)} urls")
  return new_urls

def is_url_valid(domain, url):
  if URLConfig['must_start_with']['enable']:
    if not url.startswith(URLConfig['must_start_with']['protocol']):
      debug.log(f"URL {url} is not valid, must start with {URLConfig['must_start_with']['protocol']}")
      return False

  if ("http" not in url or "https" not in url) and URLConfig['must_contain']['https']:
    debug.log(f"URL {url} is not valid, must contains of https")
    return False

  # Check if the url must contains of www
  if "www" not in url and URLConfig['must_contain']['www']:
    debug.log(f"URL {url} is not valid, must contains of www")
    return False

  # If the url not contains of domain, it's not valid
  if domain not in url and URLConfig['must_contain']['domain']:
    debug.log(f"URL {url} is not valid, must contains of {domain}")
    return False

  debug.log(f"URL {url} is valid")

  return True