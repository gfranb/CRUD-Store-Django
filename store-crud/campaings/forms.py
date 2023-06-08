from django import forms

class CreateNewCampaing(forms.Form):
    name = forms.CharField(label="Campaing Name", max_length=200, widget=forms.TextInput(attrs={
        'class':'input'}))
    