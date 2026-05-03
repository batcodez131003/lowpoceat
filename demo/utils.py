# demo/utils.py
import random
from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(user, otp):
    subject = 'Your OTP for Email Verification'
    message = f'Your OTP is {otp}. Please use this to verify your email.'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    try:
        send_mail(subject, message, email_from, recipient_list)
    except SMTPException as exc:
        if settings.DEBUG:
            # In dev, print OTP to console if SMTP auth fails.
            print(f"Email delivery failed: {exc}")
            print(f"OTP for {user.email}: {otp}")
            return True
        raise
