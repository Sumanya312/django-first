from django import forms

from .models import shorten

class bitlyForm(forms.ModelForm):
	class Meta:
		model = shorten
		fields = ['long_url']

class editBitly(forms.ModelForm):
	class Meta:
		model = shorten
		fields = ["long_url", "shortcode"]