import unittest
from utils.generate_agent import get_user_agent, generate_user_agent

class TestGenerateAgent(unittest.TestCase):
  def test_generate_user_agent(self):
    user_agent = generate_user_agent()
    list_agent = get_user_agent()

    self.assertIn(user_agent, list_agent)

  def test_generate_user_agent_out_of_range(self):
    user_agent = "IPhone 15 Pro Max"
    list_agent = get_user_agent()

    self.assertNotIn(user_agent, list_agent)

  def test_user_agent_merge_from_txt_file(self):
    path = 'tests/user_agent.txt'
    merged_list_agent = get_user_agent(path)
    list_agent = get_user_agent()

    self.assertNotEqual(merged_list_agent, list_agent)
    self.assertEqual(len(merged_list_agent), len(list_agent) + 1)

  def test_user_agent_merge_from_txt_file_empty(self):
    path = 'tests/user_agent_empty.txt'
    merged_list_agent = get_user_agent(path)
    list_agent = get_user_agent()

    self.assertEqual(merged_list_agent, list_agent)

if __name__ == '__main__':
  unittest.main()