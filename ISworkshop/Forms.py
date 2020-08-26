from django import forms
from .models import Profile

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['email', 'student_number', 'last_name', 'first_name', 'graduation_year', 'date_joined', 'last_login',
                  'degree', 'program', 'image', 'city', 'CAPES_miles_points']

