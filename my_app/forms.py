from django import forms
from .models import Comment
class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=255, label="To'liq ismingiz")
    email = forms.EmailField(max_length=255, label="E-pochta manzili")
    phone = forms.CharField(max_length=255, label="Telefon raqamingiz")
    text = forms.CharField(max_length=255, label="Xabar matni")

class AddCommentForm(forms.ModelForm):
    comment=forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols': 100}))
    stars_given=forms.IntegerField(min_value=1, max_value=5)
    class Meta:
        model=Comment
        fields=['comment','stars_given']