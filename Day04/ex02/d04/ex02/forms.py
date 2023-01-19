from django import forms

class MyForm( forms.Form ):
	input = forms.CharField( required = True, label = "input" )
