from django.db import models
# Create your models here.

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length = 50, blank = True, null = True)
    time_stamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    update = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.email
