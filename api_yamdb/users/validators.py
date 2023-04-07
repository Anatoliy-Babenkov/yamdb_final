from re import match

from rest_framework.serializers import ValidationError


def username_validation(value):
    """Имя пользователя me недопустимо.
    Разрешены символы: "@", ".", "+", "-", "_"
    """
    if value == 'me':
        raise ValidationError('Имя пользователя "me" недопустимо')
    check = match('^[\\w.@+-]+', value)
    if check is None or check.group() != value:
        forbidden_symbol = value[0] if (
            check is None
        ) else value[check.span()[1]]
        raise ValidationError(f'{forbidden_symbol} символ в имени пользователя'
                              'Имя пользователя может содержать только буквы,'
                              ' цифры, символы: "@", ".", "+", "-", "_".')
    return value
