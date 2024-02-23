from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    """Регистрация"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verify')

    def form_valid(self, form):
        new_user = form.save()
        new_user.is_active = False
        new_user.save()
        token = get_random_string(32)
        verification_url = reverse('users:verification', args=[token])
        new_user.token = token
        send_mail(
            subject='Подтверждение почты SkyStore',
            message=f'Пожалуйста, перейдите по ссылке для подтверждения почты: '
                    f'{settings.HOST}{verification_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class VerificationView(TemplateView):
    """Регистрация"""
    template_name = 'users/verification.html'


class EmailVerify(View):
    def get(self, request, *args, **kwargs):
        user_token = self.kwargs.get('token')
        our_token = User.objects.filter(token=user_token).first()
        print(our_token)
        new_user = User.objects.filter(email=our_token).first()
        print(new_user)

        if our_token:
            new_user.is_active = True
            new_user.save()
            return redirect('users:login')
        else:
            return redirect('users:verify_error')


class ProfileView(UpdateView):
    """ редактирование """
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class PasswordChangeView(TemplateView):
    template_name = 'users/password_reset.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        new_password = User.objects.make_random_password()
        send_mail(
            subject='Новый пароль аккаунта SkyStore',
            message=f'{new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        user = User.objects.get(email=email)
        print(user)
        user.set_password(new_password)
        user.save()
        return redirect('users:login')


