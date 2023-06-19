from django.urls import path, reverse_lazy
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, generate_password
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = "users"


urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", RegisterView.as_view(), name="registration"),
    path("profile/", UserUpdateView.as_view(), name="profile"),
    path("profile/generate_password", generate_password, name="generate_password"),

    path('password-reset/', PasswordResetView.as_view(
        template_name="users/registration/password_reset_form.html",
        email_template_name="users/registration/password_reset_email.html",
        success_url=reverse_lazy('users:password_reset_done')),
        name='password_reset'),

    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name="users/registration/password_reset_done.html"),
        name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name="users/registration/password_reset_confirm.html",
        success_url=reverse_lazy("users:password_reset_complete")),
         name='password_reset_confirm'),

    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name="users/registration/password_reset_complete.html"),
        name='password_reset_complete'),
]

