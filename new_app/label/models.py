from django import forms
from ..models import Label

class LableForm(forms.ModelForm):
    timestamp_url = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Please paste url here...",
            }
        ),
        label="timestamp url",
    )

    class Meta:
        model = Label
        exclude = ("stream_oid", "owner", "timestamp")
        