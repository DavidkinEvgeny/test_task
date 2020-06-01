from django.core.mail import send_mail


def send(title, content, date_event):
    send_mail(
        title,
        f'{content}, {date_event}',
        'davidkinevgeny@gmail.com',
        ['realtordavidkin@gmail.com'],
        fail_silently=False,
    )
