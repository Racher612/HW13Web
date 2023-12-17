from django import forms
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

from HW1.models import Profile


class settingsForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    avatar = forms.ImageField(allow_empty_file = True, required = False)

    class Meta:
        model = User
        fields = ["username", "email"]

    def badsave(self, **kwargs):
        user = super().save(**kwargs)
        print("before: ", user)
        user.delete()
        print("after: ", user)
        profile = Profile.objects.filter(user=user)[0]
        print(user, profile)
        print("avatar: ", profile.avatar)
        recieved_avatar =  self.cleaned_data.get("avatar")
        if recieved_avatar:
            profile.avatar = recieved_avatar
            profile.save()

        return user

    def save(self, request, **kwargs):
        print(request.FILES)
        recieved_avatar = self.cleaned_data.get("avatar")
        user = request.user
        profile = Profile.objects.filter(user = user)[0]
        user.username = self.cleaned_data.get("username")
        user.email = self.cleaned_data.get("email")
        user.save(update_fields = ['username', 'email'])
        if recieved_avatar:
            file = request.FILES[list(request.FILES.keys())[0]]
            file_name = default_storage.save(file.name, file)

            profile.avatar = "uploads/" + file.name
            profile.save(update_fields = ['avatar'])

        return user



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

