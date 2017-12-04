from django.contrib import admin

from .models import SignUp
from .forms import SignUpForm

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):#name of the class being defined doesn't matter relly
    list_display = ('email','full_name', 'time_stamp','update')#'list_diplay' is used to specify what is to be displayed in listing the model instances
    form = SignUpForm  #'form' is used to return a custom form for creation of the model SignUp
    #list_filter = ['time_stamp']
    #class Meta:
    #    model = SignUp


admin.site.register(SignUp, SignUpAdmin)
