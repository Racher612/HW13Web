from django import forms
from django.contrib.auth.models import User

from HW1.models import Profile


class settingsForm(forms.Form):
    login = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput)
    repeat = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ["login", "email", "password"]


class UploadFileForm(forms.Form):
    avatar = forms.ImageField(label = False)
    class Meta:
        model = Profile
        fields = ["avatar"]

    def save(self, **kwargs):
        user = super().save(**kwargs)
        profile = user.avatar
        print(user.avatar)
        profile.avatar = self.cleaned_data.get("avatar")
        profile.save()

        return user

