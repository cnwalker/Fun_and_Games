from django import forms
from models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('thumbnail', 'email', 'first_name', 'last_name', 'phone')
