URLConfig = {
  'must_start_with': {
    'enable': False,
    'protocol': 'https://',
  },
  'must_contain': {
    'domain': False,
    'https': True, # Bare minimum is https protocol, prevent any invalid url such javascript or data
    'www': False
  },
  'search_engine_url': [
    'https://www.bing.com/search?q=',
    'https://www.google.com/search?q=',
  ],
  'blocked_text': [
    'Please enable cookies.',
    'Our systems have detected unusual traffic from your computer network',
    'Please enable JavaScript in your browser',
    'Please enable JavaScript to view the page content.'
  ]
}