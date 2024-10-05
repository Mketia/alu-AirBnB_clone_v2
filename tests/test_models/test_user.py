import unittest
from models.user import User  # Ensure the correct path for your User model

class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Set up a User instance for testing"""
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "johndoe@example.com"
        self.user.password = "password123"

    def tearDown(self):
        """Clean up after each test"""
        del self.user

    def test_first_name(self):
        """Test the type of first_name"""
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(self.user.first_name, "John")

    def test_last_name(self):
        """Test the type of last_name"""
        self.assertEqual(type(self.user.last_name), str)
        self.assertEqual(self.user.last_name, "Doe")

    def test_email(self):
        """Test the type of email"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(self.user.email, "johndoe@example.com")

    def test_password(self):
        """Test the type of password"""
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(self.user.password, "password123")

    def test_default_values(self):
        """Test default values for optional attributes"""
        new_user = User()  # A new user without setting any attributes
        self.assertIsNone(new_user.first_name)
        self.assertIsNone(new_user.last_name)
        self.assertIsNone(new_user.email)
        self.assertIsNone(new_user.password)

if __name__ == "__main__":
    unittest.main()
