from django import forms
from django.contrib.auth import get_user_model


class UserCreationForm(forms.ModelForm):

    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ("first_name", "last_name", "username", "email", "password",
                  "password2")
        model = get_user_model()

    def clean(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if (password != password2):
            raise forms.ValidationError(
                f"The passwords do not match!")

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
