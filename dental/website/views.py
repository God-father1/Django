from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html' , {})
def about(request):
    return render(request, 'about.html', {})

def price(request):
    return render(request, 'pricing.html' , {})
def contact(request):
    if request.method == "POST":
        message_name= request.POST['message-name']
        message_email=request.POST['message-email']
        message=request.POST['message']
        return render(request, 'contact.html', {'message_name':message_name })

    #send email

        send_mail(
            message_name,#sub
            message,#message
            message_email,#from email
            ['some.doctor@gmail.com'],#toemail
            fail_silently=False,
        )
    else:
        return render(request, 'contact.html', {})

def blog(request):
    return render(request, 'blog.html' , {})
def bd(request):
    return render(request, 'blog-details.html', {})
def service(request):
    return render(request, 'service.html', {})

