from django.core.mail import send_mail
from task_sheet.celery import app
from .service import send
from .models import Sheet
from django.utils import timezone


@app.task
def send_my_email(title, content, date_event):
    send(title, content, date_event)
