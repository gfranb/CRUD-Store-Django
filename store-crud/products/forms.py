from django import forms

class CreateNewProduct(forms.Form):
    name = forms.CharField(label="Nombre del producto", max_length=200, widget=forms.TextInput(attrs={
        'class':'input'}))
    description = forms.CharField(label="Descripcion del producto", widget=forms.Textarea(attrs={'class':'input'}))
    price = forms.FloatField(label="Precio", widget=forms.NumberInput(attrs={'class':'input'}))
