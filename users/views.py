import random
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy, reverse
import config.settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from catalog.services import sendmail
from django.shortcuts import redirect
from catalog.views import TitleMixin
from django.contrib.auth import login


class LoginView(TitleMixin, BaseLoginView):
    template_name = "users/login.html"
    title = "Login"


class LogoutView(BaseLogoutView):
    template_name = "users/login.html"


class RegisterView(TitleMixin, CreateView):
    form_class = UserRegisterForm
    template_name = "users/registration/registration_form.html"
    success_url = reverse_lazy('users:registration_reset')
    title = "Registration New User"

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = reverse_lazy('users:confirm_email', kwargs={'uidb64': uid, 'token': token})
        current_site = config.settings.SITE_NAME
        sendmail(
            user.email,
            "Registration on Site!",
            f"Accept your email address. Go on: http://{current_site}{activation_url}"
        )
        return redirect('users:email_confirmation_sent')


class UserConfirmationSentView(PasswordResetDoneView):
    template_name = "users/registration/registration_sent_done.html"


class UserConfirmEmailView(View):

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('users:email_confirmed')
        else:
            return redirect('users:email_confirmation_failed')


class UserConfirmedView(TitleMixin, TemplateView):
    template_name = 'users/registration/registration_confirmed.html'
    title = "Your email is activated."


class ResetRegisterView(PasswordResetDoneView):
    template_name = "users/registration/registration_sent_done.html"


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy("users:profile")
    form_class = UserProfileForm
    template_name = "users/profile.html"

    def get_object(self, queryset=None):
        return self.request.user


def generate_password(request):
    new_password = "".join([str(random.randint(0, 9)) for _ in range(12)])
    sendmail(request.user.email, "Change password on site", new_password)
    request.user.set_password(new_password)
    return redirect(reverse("users:profile"))


class UserResetView(PasswordResetView):
    template_name = "users/registration/password_reset_form.html"
    email_template_name = "users/registration/password_reset_email.html"
    success_url = reverse_lazy('users:password_reset_done')


class UserResetDoneView(PasswordResetDoneView):
    template_name = "users/registration/password_reset_done.html"


class UserResetConfirmView(PasswordResetConfirmView):
    template_name = "users/registration/password_reset_confirm.html"
    success_url = reverse_lazy("users:password_reset_complete")


class UserResetCompleteView(PasswordResetCompleteView):
    template_name = "users/registration/password_reset_complete.html"
