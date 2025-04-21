from django import forms
from .models import Registration

# RegistrationForm - handles user input validation and processing for registrations
class RegistrationForm(forms.ModelForm):
    # Additional field for password confirmation (not in model but needed for validation)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(),  # Display as password field with hidden characters
    )
    
    # Meta class defines form behavior and connection to the model
    class Meta:
        model = Registration  # Connect form to Registration model
        # Fields to include in the form (order matters for display)
        fields = ['first_name', 'last_name', 'email', 'password', 'date_of_birth', 'phone_number']
        # Custom widgets for specific fields to enhance UI/UX
        widgets = {
            'password': forms.PasswordInput(),  # Hide password characters during input
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),  # Use HTML5 date picker
        }
    
    # Custom validation method to ensure passwords match
    def clean(self):
        # Get the cleaned data (data after basic validation)
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        # Check if passwords match and raise error if they don't
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match")
        
        return cleaned_data