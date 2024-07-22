import os
import random
import datetime
import unittest
from handlers.file import generate_file_name, write_to_file

class TestGenerateFileName(unittest.TestCase):
  def test_generate_file_name(self):
    random_number = random.randint(1000, 9999)
    date = datetime.datetime.now().strftime("%Y%m%d")
    file_name = generate_file_name(random_number)

    self.assertTrue(file_name.endswith(".txt"))
    self.assertEqual(file_name, f"urls-{date}-{str(random_number)}.txt")

  def test_generate_file_name_no_number(self):
    date = datetime.datetime.now().strftime("%Y%m%d")
    file_name = generate_file_name()

    self.assertTrue(file_name.endswith(".txt"))
    self.assertTrue(file_name.startswith(f"urls-{date}-"))

class TestWriteToFile(unittest.TestCase):
  def test_write_to_file(self):
    file_path = "tests"
    file_name = "test.txt"
    urls = [
      "https://www.google.com",
      "https://www.bing.com",
      "https://www.yahoo.com"
    ]

    write_to_file(file_name, urls, file_path, True)

    file_url = f"{file_path}/{file_name}"

    with open(file_url, "r") as file:
      data = file.readlines()

    self.assertEqual(len(data), 3)

    if os.path.exists(file_url):
      os.remove(file_url)

  def test_write_to_file_empty(self):
    file_path = "tests"
    file_name = "test.txt"
    urls = []

    write_to_file(file_name, urls, file_path, True)

    file_url = f"{file_path}/{file_name}"

    self.assertFalse(os.path.exists(file_url))

    if os.path.exists(file_url):
      os.remove(file_url)

  def test_write_to_file_no_urls(self):
    file_path = "tests"
    file_name = "test.txt"

    write_to_file(file_name, None, file_path, True)

    file_url = f"{file_path}/{file_name}"

    self.assertFalse(os.path.exists(file_url))

    if os.path.exists(file_url):
      os.remove(file_url)

if __name__ == '__main__':
  unittest.main()