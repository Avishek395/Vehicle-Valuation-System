from .models import User
from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import RadioSelect, SelectDateWidget

# User = get_user_model()


# def validate_first_name(value):
#     if value.isdigit():
#         raise ValidationError(_('Invalid . Please enter alphabets only.'))
#     if len(value) < 4:
#         raise ValidationError(
#             _('Invalid first name. First name should be more than 4 character.'))
#     if len(value) > 15:
#         raise ValidationError(
#             _('Invalid first name. First name should be less than 15 character.'))


# def validate_last_name(value):
#     if value.isdigit():
#         raise ValidationError(_('Invalid . Please enter alphabets only'))
#     if len(value) < 4:
#         raise ValidationError(
#             _('Invalid lastt name. Last name should be more than 4 character'))
#     if len(value) > 15:
#         raise ValidationError(
#             _('Invalid last name. Last name should be less than 15 character.'))


# def validate_password(value):
#     # Check password length
#     if len(value) < 8:
#         raise ValidationError(
#             "Password must be 8 character which contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
#     # Check password complexity
#     if not any(char.isdigit() for char in value) or not any(char.isupper() for char in value) or not any(char.islower() for char in value) or not any(char in '!@#$%^&*()_+.,/?><~`' for char in value):
#         raise ValidationError(
#             "Password must be 8 character which contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
#     # Check password blacklisting
#     common_passwords = ['password', '123456', 'qwerty', 'abc123']
#     if value in common_passwords:
#         raise ValidationError(
#             "Password is too common and easily guessable. Please choose a different password.")


# def validate_phone_number(value):
#     if not value.isdigit():
#         raise ValidationError(
#             _('Invalid phone number. Please enter only digits.'))
#     if len(value) != 10:
#         raise ValidationError(
#             _('Invalid phone number. The phone number must have 10 digits.'))


# class UserForm(UserCreationForm):
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'form-control'}), validators=[validate_password])
#     phone_number = forms.CharField(max_length=10, widget=forms.TextInput(
#         attrs={'class': 'form-control'}), validators=[validate_phone_number])
#     email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), validators=[
#                             EmailValidator(message='Please enter a valid email address.')])
#     first_name = forms.CharField(max_length=15, widget=forms.TextInput(
#         attrs={'class': 'form-control'}), validators=[validate_first_name])
#     last_name = forms.CharField(max_length=15, widget=forms.TextInput(
#         attrs={'class': 'form-control'}), validators=[validate_last_name])

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email',
#                   'password',  'phone_number', 'address']
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'address': forms.TextInput(attrs={'class': 'form-control'}),
#         }
# User = get_user_model()


def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError(
            _("Invalid phone number. Please enter only digits."))
    if len(value) != 10:
        raise ValidationError(
            _("Invalid phone number. The phone number must have 10 digits.")
        )


def validate_first_name(value):
    if value.isdigit():
        raise ValidationError(_("Invalid . Please enter only alphabets."))
    # if len(value)>4:
    #     raise ValidationError(_('Invalid first name. First name should be more than 4 and less than character.'))

    # raise ValidationError(_('Invalid first name. First name should be less than 30 character.'))


def validate_last_name(value):
    if value.isdigit():
        raise ValidationError(_("Invalid . Please enter only alphabets."))
    # if len(value) >4:
    #     raise ValidationError(_('Invalid last name. Last name should be more than 4 character.'))
    # if len(value) <30:
    #     raise ValidationError(_('Invalid last name. First name should be less than 30 character.'))


class UserForm(UserCreationForm):
    # phone_number = forms.CharField(
    #     max_length=10,
    #     widget=forms.TextInput(attrs={"class": "form-control"}),
    #     validators=[validate_phone_number],
    # )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        validators=[EmailValidator(
            message="Please enter a valid email address.")],
    )
    first_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        validators=[validate_first_name],
    )
    last_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        validators=[validate_last_name],
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2"

        ]
        # widgets = {

        #     "username": forms.TextInput(attrs={"class": "form-control"}),
        #     "email": forms.EmailInput(attrs={"class": "form-control"}),
        #     "password1": forms.PasswordInput(attrs={"class": "form-control"}),
        #     "password2": forms.PasswordInput(attrs={"class": "form-control"}),

        #     "first_name": forms.TextInput(attrs={"class": "form-control"}),
        #     "last_name": forms.TextInput(attrs={"class": "form-control"}),

        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        max_length=254,
        widget=forms.TimeInput(
            attrs={"name": "username", "class": "form-control", "autofocus": True}
        ),
    )
    password = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(
            attrs={"name": "password", "class": "form-control"}),
    )

