from django import forms
from .models import Comment
class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=255, label="To'liq ismingiz")
    email = forms.EmailField(max_length=255, label="E-pochta manzili")
    phone = forms.CharField(max_length=255, label="Telefon raqamingiz")
    text = forms.CharField(max_length=255, label="Xabar matni")

class AddCommentForm(forms.ModelForm):
    from django import forms

class AddCommentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'cols': 100, 'placeholder': 'Joy uchun atalgan izohlaringizni kiriting'}),
        label='Sharx'
    )
    stars_given = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Joyni  1 dan  5 gacha raqamlar bilan baholang (1-5)'}),
        min_value=1,
        max_value=5,
        label='Reyting uchun baho'
    )

    class Meta:
        model=Comment
        fields=['comment','stars_given']