import random
import datetime
from config.app import FILEPATHConfig

def generate_file_name():
  now = datetime.datetime.now()
  date = now.strftime("%Y%m%d")
  random_number = random.randint(1000, 9999)

  return f"urls-{date}-{str(random_number)}.txt"

def write_to_file(file_name, urls):
  if not urls or len(urls) == 0:
    print("Data urls is empty, nothing to write to file, skipping process")
    return

  file = open(f"{FILEPATHConfig['output_path']}/{file_name}", "w")

  for url in urls:
    file.write(url + "\n")

  file.close()

  print(f"File {file_name} has been created with {len(urls)} urls")