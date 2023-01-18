"""Test for models."""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'test@pass123'
        get_user_model().objects.create_user(email, password).save()
        user = get_user_model().objects.get(email=email)
        print(user)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        test_emails = [
            ['test1@exAMPLE.com ', 'test1@example.com'],
            [' Test2@Example.com ', 'Test2@example.com'],
            [' TEST3@EXAMPLE.COM', 'TEST3@example.com'],
        ]

        for input_email, expected_email in test_emails:
            user = get_user_model().objects.create_user(input_email,
                                                        'sample123')
            self.assertEqual(user.email, expected_email)

    def test_create_superuser(self):
        """Test create new superuser"""
        email = 'test@example.com'
        user = get_user_model().objects.create_superuser(email, 'Pass@123')

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
