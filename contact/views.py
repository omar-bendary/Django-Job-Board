from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def contact(request):

    if request.method == 'POST':
        subject = request.POST['subject']
        from_email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            from_email,
            [settings.EMAIL_HOST_USER],
        )

    return render(request, 'contact.html')
