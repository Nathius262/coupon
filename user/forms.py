from django import forms
from django.core.exceptions import ObjectDoesNotExist
from allauth.account.forms import SignupForm
from .models import CustomUser, ReferralList, VendorProfile
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from pipay.models import GenerateCode, UsersBalance
from pipay.constants import currency
from pipay.utils import affilate_topup_process, query_user_id
from notifications.signals import notify

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
        
        try:
            code = GenerateCode.objects.get(coupon_code=user.code)
            code.user = user
            code.save()
        except GenerateCode.DoesNotExist:
            pass
        
        # get the referred user id
        try:
            referred_by = CustomUser.objects.get(id=refered_by)
        except CustomUser.DoesNotExist:
            referred_by = CustomUser.objects.get(username="admin") 
        user.referred_by = str(referred_by)
        user.save()
        
        # add bonus to the exiting user that has refered this user
        if user.referred_by:           
            # add new referral profile to old user referral list
            topup=3000
            affilate_topup_process(referred_by, topup)
            notify.send(user, recipient=referred_by, verb="Referral bonus", description=f"{topup} added to your affilate balance", level='info')
            
            # first generation 
            first_gen = ReferralList.objects.get(user=referred_by)
            first_gen.user_list.add(user)
            first_gen = query_user_id(first_gen)        
            # second generation
            try:
                second_generation_referral_obj =  ReferralList.objects.get(user_list=first_gen)
                second_generation_referral = query_user_id(second_generation_referral_obj)
                topup = 300
                affilate_topup_process(second_generation_referral, topup)
                notify.send(second_generation_referral_obj, recipient=second_generation_referral, verb="Referral bonus", description=f"{topup} added to your affilate balance", level='info')
                # thrid generation
                try:                    
                    third_gen_referral_obj = ReferralList.objects.get(user_list=second_generation_referral)
                    third_gen_referral = query_user_id(third_gen_referral_obj)
                    topup=100
                    affilate_topup_process(third_gen_referral, topup)
                    notify.send(second_generation_referral_obj, recipient=third_gen_referral, verb="Referral bonus", description=f"{topup} added to your affilate balance", level='info')

                except ReferralList.DoesNotExist:
                    pass
            except ReferralList.DoesNotExist:
                pass      
            
        else:
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
        