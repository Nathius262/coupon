from django import forms
from django.core.exceptions import ObjectDoesNotExist
from allauth.account.forms import SignupForm
from .models import CustomUser
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from pipay.models import GenerateCode, UsersBalance
from pipay.constants import currency

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=60, label="First Name", widget=forms.TextInput(attrs={'placeholder':'First_Name'}))
    last_name = forms.CharField(max_length=60, label="Last Name", widget=forms.TextInput(attrs={'placeholder':'Last_Name'}))
    phone_number = PhoneNumberField(
        widget= PhoneNumberPrefixWidget(attrs={'class': 'form-control rounded-3', 'id':'floatingPhoneNumber', 'placeholder':"Phone Number"})
    )
    code = forms.CharField(max_length=12, label="code", widget=forms.TextInput(attrs={'placeholder':'coupon code'}))

    class Meta:
        model = CustomUser
        fields = ("email", "username", "first_name", "last_name", 'phone_number', "code", "password1", "password2")

    
    def clean_code(self):
        code = self.cleaned_data['code']
        user = CustomUser.objects.all().filter(code=code)
        coupon_code = GenerateCode.objects.all().filter(coupon_code=code)
        if not coupon_code.exists():
            raise forms.ValidationError('code "%s" is invalid' % code)
        if user.exists():
            raise forms.ValidationError('code "%s" is already in use.' % code)
        
        return code

    def clean_username(self):
        username = self.cleaned_data['username']
        user = CustomUser.objects.all().filter(username=username)
        if user.exists():
            raise forms.ValidationError('username "%s" is already in use.' % username)
        return username

    def save(self, request):
        refered_by = request.session.get('ref_user')
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.code = self.cleaned_data['code']
        user.phone_number = self.cleaned_data['phone_number']
        
        # get the referred user id
        try:
            referred_by = CustomUser.objects.get(id=refered_by)
        except CustomUser.DoesNotExist:
            referred_by = CustomUser.objects.get(username="admin") 
        user.referred_by = str(referred_by)
        
        user.save()
        
        try:
            code = GenerateCode.objects.get(coupon_code=user.code)
            code.user = user
            code.save()
        except GenerateCode.DoesNotExist:
            pass
        
        # create new users balance
        UsersBalance.objects.get_or_create(user=user)                
        
        return user


class AccountSettingsForm(forms.ModelForm):
    
    phone_number = PhoneNumberField(
        widget= PhoneNumberPrefixWidget(attrs={'class': 'form-control rounded-3', 'id':'floatingPhoneNumber', 'placeholder':"Phone Number"})
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'picture', "phone_number")
        widgets = {
            #'picture': forms.FileInput(attrs={'class': 'form-control', 'onchange': 'readURL(this)', 'id':'id_image_file', 'hidden':'True'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-3', 'id':'floatingInput', 'placeholder':"name@example.com"}),
            'username': forms.TextInput(attrs={'class': 'form-control rounded-3', 'id':'floatingUsername', 'placeholder':"username"}),
            'first_name': forms.TextInput(attrs={'class': 'form-control rounded-3', 'id':'floatingName', 'placeholder':"First Name"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control rounded-3', 'id':'floatingName', 'placeholder':"Last Name"}),
        }

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
            except CustomUser.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account.email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)
            except CustomUser.DoesNotExist:
                return username
            raise forms.ValidationError('username "%s" is already in use.' % account.username)