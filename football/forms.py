from django.forms import ModelForm
from .models import TeamName
from django import forms

class TeamNameForm(ModelForm):
	class Meta:
		model = TeamName
		fields = '__all__'
		

		labels = {
			'team_name': "",
			'age_group': "",
			'venue': "",
			'address': "",
			'contact': "",
			'contact_mob': "",
			'contact_email': "",
			'map_link': "",
		}

		widgets = {
			'team_name': forms.TextInput(attrs={'Class': 'form-control', 'placeholder': 'Team Name'}),
			'age_group': forms.Select(attrs={'Class': 'form-control', 'placeholder': 'Age Group'}),
			'venue': forms.TextInput(attrs={'Class': 'form-control', 'placeholder': 'Venue'}),
			'address': forms.TextInput(attrs={'Class': 'form-control', 'placeholder': 'Address'}),
			'contact': forms.TextInput(attrs={'Class': 'form-control', 'placeholder': 'Contact Name'}),
			'contact_mob': forms.TextInput(attrs={'Class': 'form-control', 'placeholder': 'Contact Mobile No'}),
			'contact_email': forms.EmailInput(attrs={'Class': 'form-control', 'placeholder': 'Contact Email'}),
			'map_link': forms.TextInput(attrs={'Class': 'form-control', 'placeholder': 'Map Link'})
		}
