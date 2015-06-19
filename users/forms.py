from django import forms
from userprofiles.models import UserProfile
from userprofiles.admin import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length = 135)
    last_name = forms.CharField(max_length = 140)
    class Meta:
        model = UserProfile
        fields = ('first_name',
                  'last_name',
                  'email',
                  'chapter',
                  'password1',
                  'password2')

def save(self, commit = True):
    user = super(MyRegistrationForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    user.email = self.cleaned_data['email']
    user.first_name = self.cleaned_data['first_name']
    user.last_name = self.cleaned_data['last_name']
    user.chapter = self.cleaned_data['chapter']
    if commit:
        user.save()
    return user
        
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
