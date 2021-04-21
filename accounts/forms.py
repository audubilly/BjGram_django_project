from django import forms

from accounts.models import Owner


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = "__all__"
