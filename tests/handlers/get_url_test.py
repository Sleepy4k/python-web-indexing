import unittest
from handlers.get_url import generate_query, bypass_safe_search

class TestGenerateQuery(unittest.TestCase):
  def test_generate_query(self):
    domain = 'google.com'
    keyword = 'google'
    search_engine = 'google'
    query = generate_query(domain, keyword, search_engine)

    self.assertEqual(query, 'site:google.com google')

  def test_generate_query_bing(self):
    domain = 'google.com'
    keyword = 'google'
    search_engine = 'bing'
    query = generate_query(domain, keyword, search_engine)

    self.assertEqual(query, 'sites:google.com google')

class TestBypassSafeSearch(unittest.TestCase):
  def test_bypass_safe_search_google(self):
    url = 'https://www.google.com'
    new_url = bypass_safe_search(url)

    self.assertEqual(new_url, 'https://www.google.com&safe=off')

  def test_bypass_safe_search(self):
    url = 'https://www.bing.com'
    new_url = bypass_safe_search(url)

    self.assertEqual(new_url, 'https://www.bing.com&SafeSearch=off')

if __name__ == '__main__':
  unittest.main()