import unittest
from config.user_agent import get_user_agent
from utils.generate_agent import generate_user_agent

class TestGenerateAgent(unittest.TestCase):
  def test_generate_user_agent(self):
    user_agent = generate_user_agent()
    list_agent = get_user_agent()

    self.assertIn(user_agent, list_agent)

  def test_user_agent_merge_from_txt_file(self):
    path = 'tests/user_agent.txt'
    merged_list_agent = get_user_agent(path)
    list_agent = get_user_agent()

    self.assertNotEqual(merged_list_agent, list_agent)
    self.assertEqual(len(merged_list_agent), len(list_agent) + 1)
