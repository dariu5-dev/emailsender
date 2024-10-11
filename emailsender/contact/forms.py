from django import forms


class contactForm(forms.Form):
        name = forms.CharField(max_length=100)
        email = forms.EmailField()
        subject = forms.CharField(max_length=500)
        message = forms.CharField(widget=forms.Textarea)