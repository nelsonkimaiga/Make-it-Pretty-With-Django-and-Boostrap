from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
	class Meta:
	#	fields =  ['fullname', 'email', 'age']
		exclude = ['last_update']
		model = Student

	def clean_age(self):
	    age = self.cleaned_data.get('age')
	    if age > 120:
	        raise form.ValidationError("You may be too old for this class")
	    return age
