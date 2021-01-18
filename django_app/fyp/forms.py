from django import forms



class QueryImageForm(forms.Form):
		image = forms.ImageField()