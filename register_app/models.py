from django.db import models

# Registration model - defines the database schema for storing user registration data
class Registration(models.Model):
    # Basic personal information fields
    first_name = models.CharField(max_length=100)  # First name with maximum 100 characters
    last_name = models.CharField(max_length=100)   # Last name with maximum 100 characters
    
    # Contact information with validation
    email = models.EmailField(unique=True)  # Email must be unique to prevent duplicate registrations
    phone_number = models.CharField(max_length=15, blank=True)  # Optional phone number field
    
    # Additional information
    date_of_birth = models.DateField(null=True, blank=True)  # Optional date of birth
    
    # Temporary password field with null=True to allow migration to work
    password = models.CharField(max_length=128, null=True, blank=True)
    
    # Metadata - automatically tracks when the registration was created
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-populated with current time on creation
    
    # String representation of this model for admin interface and debugging
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
