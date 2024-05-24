""" Test  for user Model"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """ Test MOdels """
    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    def test_new_user_email_normalize(self):
        """Test email is normailized for new user"""
        sample_emails=[
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@EXAMPLE.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        
        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(email, 'Faiz123')
            self.assertEqual(user.email, expected_email)