import os
import random
import datetime
from config.app import FILEPATHConfig

def generate_file_name(number=None):
  now = datetime.datetime.now()
  date = now.strftime("%Y%m%d")
  random_number = number or random.randint(1000, 9999)

  return f"urls-{date}-{str(random_number)}.txt"

def write_to_file(file_name, urls, path=None, test=False):
  if not urls or len(urls) == 0:
    not test and print("Data urls is empty, nothing to write to file, skipping process")
    return

  path = path or FILEPATHConfig['output_path']

  not os.path.exists(path) and os.makedirs(path)
  not os.path.exists(f"{path}/{file_name}") and open(f"{path}/{file_name}", "w").close()

  file = open(f"{path}/{file_name}", "w")

  for url in urls:
    file.write(url + "\n")

  file.close()

  not test and print(f"File {file_name} has been created with {len(urls)} urls")