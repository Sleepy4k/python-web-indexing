import unittest
from tests.check_url_test import TestCheckURL
from tests.generate_agent_test import TestGenerateAgent

def main():
  loader = unittest.TestLoader()
  test_case = [
    loader.loadTestsFromTestCase(TestCheckURL),
    loader.loadTestsFromTestCase(TestGenerateAgent)
  ]

  suite = unittest.TestSuite(test_case)

  runner = unittest.TextTestRunner(verbosity=2)
  runner.run(suite)

if __name__ == '__main__':
  main()