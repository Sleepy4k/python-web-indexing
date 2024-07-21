import random
import utils.debug as debug
from config.user_agent import get_user_agent

def generate_user_agent():
  list_agent = get_user_agent()
  length = len(list_agent) - 1
  user_agent = list_agent[random.randint(0, length)]
  debug.log("User agent generated: " + user_agent)

  return user_agent
