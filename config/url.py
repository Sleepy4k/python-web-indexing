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
    'Please click the checkbox',
    'Please verify you are a human',
    'Please prove that you are human',
    'Please enable JavaScript in your browser',
    'Please turn JavaScript on and reload the page',
    'Please enable JavaScript to view the page content.',
    'Our systems have detected unusual traffic from your computer network',
  ]
}