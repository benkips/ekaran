from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'index.html', {})


def services(request):
    return render(request, 'services.html', {})


def portfolio(request):
    return render(request, 'portfolio.html', {})


def blog(request):
    return render(request, 'blog.html', {})


# def contact(request):
#     return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})

def contact(request):

    if request.method=='POST':
        message_name= request.POST['name']
        message_email=request.POST['email']
        message_subject=request.POST['subject']
        message_message=request.POST['message']

        send_mail(message_subject,message_name+""+message_message,message_email,['info@ekarantechnologies.com'],fail_silently=False)

        return  render(request,'contact.html',{"name":message_name})

    else:

        return render(request,'contact.html',{})


