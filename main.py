from handlers.get_url import get_data_from_search_engine
from handlers.file import generate_file_name, write_to_file

def main():
  # Clear the screen
  print("\033[H\033[J")

  print("Python Web Information Gathering")
  print("=====================================")
  domain = input("Enter domain: ")
  keyword = input("Enter keyword: ")
  print("=====================================")
  print("Searching for urls...")
  urls = get_data_from_search_engine(domain, keyword)
  file_name = generate_file_name()
  print("=====================================")
  write_to_file(file_name, urls)
  print("=====================================")

if __name__ == "__main__":
  main()
