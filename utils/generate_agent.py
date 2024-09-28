import random
import utils.debug as debug
from config.app import FILEPATHConfig
from config.user_agent import USERAGENT

used_user_agent = []

def get_user_agent(path=None, test=False) -> list:
  """ Get user agent from the file and merge it with the default user agent
  Args:
    path (str): Path to the user agent file
    test (bool): If true, the function will return the default user agent
  Returns:
    list: List of user agent
  """
  if test and not path:
    return USERAGENT

  if not test and not path:
    path = FILEPATHConfig['user_agent']

  try:
    file = open(path, 'r')
  except FileNotFoundError:
    return USERAGENT

  user_agent = file.readlines()

  if not user_agent or len(user_agent) == 0:
    return USERAGENT

  file.close()

  return USERAGENT + user_agent

def generate_user_agent() -> str:
  """ Generate user agent randomly from the list of user agent
  Returns:
    str: User agent
  """
  if len(used_user_agent) == len(USERAGENT):
    used_user_agent.clear()

  list_agent = get_user_agent()
  length = len(list_agent) - 1
  user_agent = list_agent[random.randint(0, length)]
  debug.log("User agent generated: " + user_agent)

  if user_agent in used_user_agent:
    return generate_user_agent()

  # Make sure the user agent doesn't contain newline
  user_agent = user_agent.replace("\n", "")

  return user_agent
