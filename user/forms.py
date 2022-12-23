from django import forms
from allauth.account.forms import SignupForm
from .models import User


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=60, label="First Name", widget=forms.TextInput(attrs={'placeholder':'First_Name'}))
    last_name = forms.CharField(max_length=60, label="Last Name", widget=forms.TextInput(attrs={'placeholder':'Last_Name'}))

    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name", "code", "password1", "password2")


    def save(self, request):
        refered_by = request.session.get('ref_user')
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        try:
            user.referred_by = str(User.objects.get(id=refered_by))
        except:
            user.referred_by = ''
        user.save()

        return user


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'picture')
        widgets = {
            'picture': forms.FileInput(attrs={'class': 'form-control', 'onchange': 'readURL(this)', 'id':'id_image_file', 'hidden':'True'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-3', 'id':'floatingInput', 'placeholder':"name@example.com"}),
            'username': forms.TextInput(attrs={'class': 'form-control rounded-3', 'id':'floatingUsername', 'placeholder':"username"}),
            'first_name': forms.TextInput(attrs={'class': 'form-control rounded-3', 'id':'floatingName', 'placeholder':"First Name"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control rounded-3', 'id':'floatingName', 'placeholder':"Last Name"}),
        }

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account.email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError('username "%s" is already in use.' % account.username)