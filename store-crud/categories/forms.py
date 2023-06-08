from django import forms

class CreateNewCategory(forms.Form):
    name = forms.CharField(label="Category Name", max_length=200, widget=forms.TextInput(attrs={
        'class':'input'}))
