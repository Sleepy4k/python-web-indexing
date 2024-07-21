import inspect
import datetime
from config.app import DEBUGConfig, FILEPATHConfig

def log(message):
  if not DEBUGConfig['debug']:
    return

  now = datetime.datetime.now()
  data = f"[DEBUG] [{now.strftime('%Y-%m-%d %H:%M:%S')}] {message}"

  if DEBUGConfig['verbose']:
    data += (
      "\n=====================\n"
      "[VERBOSE] Data:\n"
      f"\tCaller: def {inspect.stack()[1][3]}():\n"
      f"\tLine: {inspect.stack()[1][2]}\n"
      f"\tFile: {inspect.stack()[1][1]}\n"
    )

  file = open(f"{FILEPATHConfig['log_path']}/log-{now.strftime('%Y%m%d')}.txt", 'a')
  file.write(data + "\n")
  file.close()
