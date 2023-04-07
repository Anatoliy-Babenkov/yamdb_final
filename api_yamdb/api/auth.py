from django.conf import settings
from django.core.mail import send_mail


def send_confirmation_code(user, token):
    """Отправляет код на почту."""
    send_mail(subject='yamdb регистрация',
              message=f'Код подтверждения: {token}',
              from_email=settings.CONF_EMAIL,
              recipient_list=[user.email]
              )
