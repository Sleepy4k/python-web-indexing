from config.app import APPConfig
from handlers.get_url import get_data_from_search_engine
from handlers.file import generate_file_name, write_to_file

def main():
  print("\033[H\033[J")
  print(f"Welcome to {APPConfig['name']} v{APPConfig['version']}")
  print(f"{APPConfig['description']}")
  print(f"Developed by {APPConfig['author']} ({APPConfig['github']})")
  print("=====================================")
  domain = input("Enter domain (use * for wildcard): ")
  keyword = input("Enter keyword (ex: best movie): ")
  print("=====================================")
  print("Searching for urls...")
  urls = get_data_from_search_engine(domain, keyword)
  file_name = generate_file_name()
  print("=====================================")
  write_to_file(file_name, urls)
  print("=====================================")

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("\nExiting...")
    exit(0)
