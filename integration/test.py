import unittest
from main import UserManager

class TestUserManager(unittest.TestCase):

    def setUp(self):
        # Set up a temporary database for testing
        self.manager = UserManager(':memory:')

    def tearDown(self):
        self.manager.close()

    def test_crud_operations(self):
        # Insert user
        self.manager.insert_user('Test User', 20)
        users = self.manager.get_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][1], 'Test Userr')
        self.assertEqual(users[0][2], 20)

        # Update user
        user_id = users[0][0]
        self.manager.update_user(user_id, 'Updated User', 21)
        users = self.manager.get_users()
        self.assertEqual(users[0][1], 'Updated User')
        self.assertEqual(users[0][2], 21)

        # Delete user
        self.manager.delete_user(user_id)
        users = self.manager.get_users()
        self.assertEqual(len(users), 0)

if __name__ == '__main__':
    unittest.main()
