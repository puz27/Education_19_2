import random
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from catalog.services import sendmail
from django.shortcuts import redirect
from users.forms import UserForgotPasswordForm, UserSetNewPasswordForm


class LoginView(BaseLoginView):
    template_name = "users/login.html"


class LogoutView(BaseLogoutView):
    template_name = "users/login.html"


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/registration.html"
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Registration New User"
        return context

    def form_valid(self, form):
        new_user = form.save()
        sendmail(new_user.email, "Success registration!", "You made success registration!")
        return super().form_valid(form)


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


# class UserResetView(SuccessMessageMixin, PasswordResetView):
#     form_class = UserResetForm
#     template_name = "users/reset_password.html"
#     success_url = reverse_lazy('')
#     success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["Title"] = "Reset Password"
#         return context

#
# class UserResetView(PasswordResetView):
#     pass
#
#
# class UserResetSentView(PasswordResetDoneView):
#     pass
#
#
# class UserResetConfirmView(PasswordResetConfirmView):
#     pass
#
#
# class UserResetCompleteView(PasswordResetCompleteView):
#     pass

