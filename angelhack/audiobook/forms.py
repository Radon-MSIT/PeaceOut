from django import forms

from .models import Info

class InfoForm(forms.ModelForm):
	class Meta:
		model = Info
		fields = ['Full_Name', 'email', 'Phone_No', 'City', 'Religion']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email

	def clean_Full_Name(self):
		Full_Name = self.cleaned_data.get('Full_Name')
		return Full_Name

	def clean_Religion(self):
		Religion = self.cleaned_data.get('Religion')
		return Religion

	def clean_Phone_No(self):
		Phone_No = self.cleaned_data.get('Phone_No') 
		
		if (len(Phone_No) < 10 and not Phone_No.isdigit()):
			raise forms.ValidationError("Please enter a valid phone number")
		
		if (len(Phone_No) < 10):
			raise forms.ValidationError("Please enter a 10 digits number")	  
		
		if not Phone_No.isdigit(): 
			raise forms.ValidationError("Please enter a valid phone number")
		
		return Phone_No