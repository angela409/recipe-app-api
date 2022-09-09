"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

<<<<<<< HEAD
=======

>>>>>>> 4389094 (Create User Model)
def test_create_user_with_email_success(self):
    """Test creating a user with an email is success."""
    email = 'test@example.com'
    password = 'testpass123'
    user = get_user_model().objects.create_user(
        email=email,
        password=password,
    )

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))

<<<<<<< HEAD
=======

>>>>>>> 4389094 (Create User Model)
def test_new_user_email_normalized(self):
    """Test email is normalized for new users."""
    sample_emails = [
        ['test1@EXAMPLE.com', 'test1@example.com'],
        ['Test2@Example.com', 'Test2@example.com'],
        ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
        ['test4@example.COM', 'test4@example.com'],
    ]

    for email, expected in sample_emails:
        user = get_user_model().objects.create_user(email, 'sample123')
<<<<<<< HEAD
        self.assertEqual(user.email, expected)
=======
        self.assertEqual(user.email, expected)
>>>>>>> 4389094 (Create User Model)
