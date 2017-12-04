from django.shortcuts import render
from django.core.mail import send_mail

from .forms import SignUpForm, ContactForm
from django.conf import settings

from .models import SignUp

# Create your views here.
#views also does some job on the data we enter...

def home(request):
    name_user = request.user
    list_signups = SignUp.objects.all()
    title = 'SIGN UP NOW!!!'
    form_var = SignUpForm(request.POST or None)#if "or None" is not added then some question around fields appear.(validation)

    if form_var.is_valid():
        instance = form_var.save(commit = False)#commit = False;allows to hold the data before saving to db & do some processing
        inst_full_name = form_var.clean_full_name()
        if not inst_full_name:
            instance.full_name = "Unknown Jack"
        instance.save()
        #form_var.save()
        title = "You Are Registered"

    context = {    #'context' is a ""context_variable""(takes the form of a dictionary) which allows us to use other variables ('title' above) or objects, inside the templates(eg:home.html)
        'template_title':title,
        'form':form_var,
        'signup_list':list_signups,
        'name':name_user,
    }

    return render(request, 'newsletter/home.html', context)

def contact(request):#this view is for submitting contact details and automatically sending mails to registered mail id's...
    form_var = ContactForm(request.POST or None)
    title_var = "Contact Us"
    title_align_center = False#set to True to align the title for contact form to center
    context = {
        'form':form_var,
        'title':title_var,
        'title_align_center':title_align_center
    }

    if form_var.is_valid():
        #for key in form_var.cleaned_data:
        #    print(key + ': ' + form_var.cleaned_data[key])
        mail_sender = settings.EMAIL_HOST_USER
        mail = form_var.cleaned_data.get("email")
        message = form_var.cleaned_data.get("message")
        name = form_var.cleaned_data.get("full_name")
        #print(name,mail,message)
        send_mail('Contact Acknowledgement',
            'Thank you for Query!!. We will ping you soon. ('  + message +  ') ' + 'Mr.' + name,
             mail_sender,
             [mail],
             fail_silently = True,
        )

    return render(request,'newsletter/contact.html',context)
