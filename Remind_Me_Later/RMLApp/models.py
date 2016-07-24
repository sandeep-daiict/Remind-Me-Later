from django.db import models
from django.core.validators import RegexValidator
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone
# Create your models here.
@python_2_unicode_compatible
class RemindMe(models.Model):
    remind_message = models.TextField()
    remind_date = models.DateTimeField('date to Remind', null=False)
    remind_email = models.EmailField(max_length=254,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    remind_phone = models.CharField(max_length = 15, validators=[phone_regex], blank=True) # validators should be a list

    def __str__(self):
        return self.remind_message + " at " + self.remind_date.strftime("%B %d, %Y")

    def to_be_reminded_in_an_hour(self):
        return self.remind_date >= timezone.now() - datetime.timedelta(hours=1)