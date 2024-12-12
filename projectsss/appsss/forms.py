# appsss/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role', 'department', 'student_id_image', 'study_load_image', 'employee_id_image', 'document_image']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['student_id_image'].required = False
        self.fields['study_load_image'].required = False
        self.fields['employee_id_image'].required = False
        self.fields['document_image'].required = False

        self.fields['role'].widget = forms.Select(choices=Profile.ROLE_CHOICES)
        self.fields['department'].widget = forms.Select(choices=Profile.DEPARTMENT_CHOICES)
