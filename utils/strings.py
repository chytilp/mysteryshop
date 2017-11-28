from django.conf import settings


def normalize_phone_number(number):
    if number:
        number = number.replace(' ', '').replace('-', '')
        if len(number) == 9:
            number = ''.join((settings.DEFAULT_CALLING_CODE, number))
        elif len(number) == 14 and number.startswith('00'):
            number = '+' + number[2:]
        elif len(number) == 12 and number.startswith('420'):
            number = '+' + number
        if not ((len(number) == 13 and number.startswith('+') and number[1:].isdigit()) or number == ''):
            raise ValueError(_('Phone number is not in valid format'))
    return number
