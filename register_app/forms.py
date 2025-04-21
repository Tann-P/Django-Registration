from django import forms
from .models import Registration

# RegistrationForm - handles user input validation and processing for registrations
class RegistrationForm(forms.ModelForm):
    # Meta class defines form behavior and connection to the model
    class Meta:
        model = Registration  # Connect form to Registration model
        # Fields to include in the form (order matters for display)
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'phone_number']
        # Custom widgets for specific fields to enhance UI/UX
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),  # Use HTML5 date picker
        }