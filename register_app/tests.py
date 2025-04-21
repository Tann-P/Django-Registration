from django.test import TestCase, Client
from django.urls import reverse
from .models import Registration
from .forms import RegistrationForm
from datetime import date

class RegistrationModelTests(TestCase):
    """Test cases for the Registration model"""
    
    def test_registration_creation(self):
        """Test that a Registration instance can be created with required fields"""
        registration = Registration.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            password="securepassword123"
        )
        self.assertEqual(registration.first_name, "John")
        self.assertEqual(registration.last_name, "Doe")
        self.assertEqual(registration.email, "john.doe@example.com")
        self.assertEqual(str(registration), "John Doe")  # Test __str__ method

class RegistrationFormTests(TestCase):
    """Test cases for the RegistrationForm"""
    
    def test_valid_form(self):
        """Test form with valid data"""
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com',
            'password': 'securepass123',
            'password_confirm': 'securepass123',
            'date_of_birth': '1990-01-01',
            'phone_number': '123-456-7890'
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_passwords_mismatch(self):
        """Test form validation when passwords don't match"""
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com',
            'password': 'securepass123',
            'password_confirm': 'differentpassword',
            'date_of_birth': '1990-01-01',
            'phone_number': '123-456-7890'
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password_confirm', form.errors)
    
    def test_missing_required_fields(self):
        """Test form validation when required fields are missing"""
        form_data = {
            'first_name': '',  # Missing first name
            'last_name': 'Smith',
            'email': 'jane.smith@example.com',
            'password': 'securepass123',
            'password_confirm': 'securepass123',
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)

class RegistrationViewTests(TestCase):
    """Test cases for the registration views"""
    
    def setUp(self):
        self.client = Client()
        
    def test_form_view_get(self):
        """Test that the form page loads correctly"""
        response = self.client.get(reverse('form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')
        self.assertIsInstance(response.context['form'], RegistrationForm)
    
    def test_form_view_post_success(self):
        """Test successful registration submission"""
        form_data = {
            'first_name': 'Bob',
            'last_name': 'Johnson',
            'email': 'bob.johnson@example.com',
            'password': 'securepass123',
            'password_confirm': 'securepass123',
            'date_of_birth': '1985-05-15',
            'phone_number': '555-123-4567'
        }
        response = self.client.post(reverse('form'), form_data)
        # Check redirect after successful form submission
        self.assertEqual(response.status_code, 302)
        
        # Verify that a registration was created in the database
        self.assertTrue(Registration.objects.filter(email='bob.johnson@example.com').exists())
    
    def test_form_view_post_invalid(self):
        """Test form submission with invalid data"""
        form_data = {
            'first_name': 'Bob',
            'last_name': 'Johnson',
            'email': 'invalid-email',  # Invalid email format
            'password': 'securepass123',
            'password_confirm': 'securepass123',
        }
        response = self.client.post(reverse('form'), form_data)
        # Check that we stay on the same page with form errors
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())
    
    def test_export_view(self):
        """Test that the export view returns an Excel file"""
        # Create test registration data first
        Registration.objects.create(
            first_name="Susan",
            last_name="Wilson",
            email="susan.wilson@example.com",
            password="securepassword123"
        )
        
        # Test the export view
        response = self.client.get(reverse('export_excel'))
        # Check that response is a file download
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response['Content-Type'], 
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        self.assertIn('attachment; filename="registrations_', response['Content-Disposition'])
