import unittest
from tests.utils.generate_agent_test import TestGenerateAgent
from tests.handlers.file_test import TestGenerateFileName, TestWriteToFile
from tests.utils.check_url_test import TestCheckDuplicateURL, TestIsURLValid
from tests.handlers.get_url_test import TestGenerateQuery, TestBypassSafeSearch

def main():
  loader = unittest.TestLoader()
  test_case = [
    # Load Check URL Test
    loader.loadTestsFromTestCase(TestIsURLValid),
    loader.loadTestsFromTestCase(TestCheckDuplicateURL),

    # Load Agent Test
    loader.loadTestsFromTestCase(TestGenerateAgent),

    # Load File Test
    loader.loadTestsFromTestCase(TestWriteToFile),
    loader.loadTestsFromTestCase(TestGenerateFileName),

    # Load Get URL Test
    loader.loadTestsFromTestCase(TestGenerateQuery),
    loader.loadTestsFromTestCase(TestBypassSafeSearch),
  ]

  suite = unittest.TestSuite(test_case)

  runner = unittest.TextTestRunner(verbosity=2)
  runner.run(suite)

if __name__ == '__main__':
  main()