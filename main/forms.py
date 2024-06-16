from django import forms
from .models import Post
from allauth.account.forms import SignupForm
from string import hexdigits
from django.conf import settings
from django.core.mail import send_mail
import random

class CommentForm(forms.ModelForm):
   class Meta:
       model = Post
       fields =  ['head', 'text']

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields =  ['head', 'text', 'category']

class CommonSignupForm(SignupForm):
    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        user.is_active = False
        code = ''.join(random.sample(hexdigits, 5))
        user.code = code
        user.save()
        send_mail(
            subject=f'Код активации',
            message=f'Код активации аккаунта: {code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email]
        )
        return user