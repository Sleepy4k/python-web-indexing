import unittest
from config.url import URLConfig
from utils.check_url import check_duplicate_urls, is_url_valid

class TestCheckDuplicateURL(unittest.TestCase):
  def test_check_duplicate_url(self):
    urls = [
      'https://www.google.com',
      'https://www.bing.com',
      'https://www.yahoo.com',
      'https://www.google.com',
      'https://www.bing.com',
      'https://www.yahoo.com',
    ]

    new_urls = check_duplicate_urls(urls)

    self.assertEqual(len(new_urls), 3)

  def test_check_duplicate_url_empty(self):
    urls = []

    new_urls = check_duplicate_urls(urls)

    self.assertEqual(len(new_urls), 0)

class TestIsURLValid(unittest.TestCase):
  def test_is_url_valid(self):
    domain = 'google.com'
    url = 'https://www.google.com'

    self.assertTrue(is_url_valid(domain, url))

  def test_is_url_valid_not_valid(self):
    domain = 'bing.com'
    url = 'http://www.google.com'

    self.assertFalse(is_url_valid(domain, url))

  def test_is_url_contains_www(self):
    URLConfig['must_contain']['www'] = True
    domain = 'www.google.com'
    url = 'https://www.google.com'

    self.assertTrue(is_url_valid(domain, url))

  def test_is_url_not_contains_www(self):
    URLConfig['must_contain']['www'] = True
    domain = 'google.com'
    url = 'https://google.com'

    self.assertFalse(is_url_valid(domain, url))

  def test_is_url_start_with_https(self):
    URLConfig['must_start_with']['enable'] = True
    URLConfig['must_start_with']['protocol'] = 'https://'
    domain = 'google.com'
    url = 'https://www.google.com'

    self.assertTrue(is_url_valid(domain, url))

  def test_is_url_not_start_with_https(self):
    URLConfig['must_start_with']['enable'] = True
    URLConfig['must_start_with']['protocol'] = 'https://'
    domain = 'google.com'
    url = 'http://www.google.com'

    self.assertFalse(is_url_valid(domain, url))

  def test_is_url_must_contains_https(self):
    URLConfig['must_contain']['https'] = True
    domain = 'google.com'
    url = 'https://www.google.com'

    self.assertTrue(is_url_valid(domain, url))

  def test_is_url_not_contains_https(self):
    URLConfig['must_contain']['https'] = True
    domain = 'google.com'
    url = 'url://www.google.com'

    self.assertFalse(is_url_valid(domain, url))

if __name__ == '__main__':
  unittest.main()