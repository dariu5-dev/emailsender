from django.shortcuts import render, redirect
from .forms import contactForm
from django.core.mail import EmailMessage, get_connection   
from django.conf import settings

# Create your views here.   

#             return redirect('success')
#     else:
#         form = contactForm()
        
#     return render(request, 'contact.html', {'form': form})

# subject = 'test'
# recipent_list = ['dariusdauda333@gmail.com', 'd34387873@gmail.com', 'basseyimoh301@gmail.com']

# def send_email(request):  
#    if request.method == "POST": 
 
#    return render(request, 'home.html')

def sendmail(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # send_mail(
            #     subject,
            #     message,
            #     email,
            #     ['d34387873@gmail.com']
            # )
        with get_connection(  
           host=settings.EMAIL_HOST, 
        port=settings.EMAIL_PORT,  
        username=settings.EMAIL_HOST_USER, 
        password=settings.EMAIL_HOST_PASSWORD, 
        use_tls=settings.EMAIL_USE_TLS  
        ) as connection:  
        #    subject = request.POST.get("subject")  
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = [email]  
        #    message = request.POST.get("message")  
           EmailMessage(subject, message, email_from, recipient_list, connection=connection).send() 
           return redirect('success')
    else:
        form = contactForm()

    return render(request, "contact.html", {'form': form})   

def success(request):
    return render(request, 'success.html')