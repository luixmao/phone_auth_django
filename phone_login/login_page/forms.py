from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#this is to custom registration form
class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ('email','password1','password2')
		
	def save(self, commit=True):
		user = super(MyRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		
		user.username = self.cleaned_data['email']

		if commit:
		    user.save()
		return user
