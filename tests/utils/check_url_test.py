import unittest
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

if __name__ == '__main__':
  unittest.main()