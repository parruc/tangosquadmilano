from django import forms
from django.contrib.auth import get_user_model
from material import Layout
from material import Row


class AdidasSignupForm(forms.ModelForm):
    layout = Layout(
        Row('username', 'email', ),
        Row('password1', 'password2', ),
        Row('first_name', 'last_name', ),
        Row('birth_date'),
        Row('image', 'phone_number'),
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'birth_date',
                  'phone_number', 'image')

    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birth_date = self.cleaned_data['birth_date']
        user.phone_number = self.cleaned_data['phone_number']
        user.image = self.cleaned_data['image']
        user.save()
