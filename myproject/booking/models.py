import datetime
from django.db import models
from django.utils import timezone
from unittest.util import _MAX_LENGTH   
#
import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from unicodedata import normalize

# Create your models here.

SERVICES = (
    ('Hair Rebond-$20', 'HAIR REBOND-$20'),
    ('Hair Dye-$20', 'HAIR DYE-$20'),
    ('Hair Cut-$7', 'HAIR CUT-$7'),
    ('Face Mask-$8', 'FACE MASK-$8'),
    ('Face Extraction-$12', 'FACE EXTRACTION-$12'),
    ('Makeup-$11', 'MAKEUP-$11'),
    ('Massage-$15', 'MASSAGE-$15'),
    ('Cut/Clean-$9', 'CUT/CLEAN-$9'),
    ('Foot Spa-$10', 'FOOT SPA-$10'),
)

TIME_CHOICES = (
    ('9:00 - 9:30', '9:00 - 9:30'),
    ('9:31 - 10:00', '9:31 - 10:00'),
    ('10:31 - 11:00', '10:31 - 11:00'),
    ('11:01 - 11:30', '11:01 - 11:30'),
    ('11:31 - 12:30', '11:31 - 12:30'),
    ('12:31 - 13:00', '12:31 - 13:00'),
    ('13:01 - 13:30', '13:01 - 13:30'),
    ('13:31 - 14:00', '13:31 - 14:00'),
    ('14:01 - 14:30', '14:01 - 14:30'),
    ('14:31 - 15:00', '14:31 - 15:00'),
    ('15:01 - 15:30', '15:01 - 15:30'),
    ('15:31 - 16:00', '15:31 - 16:00'),
    ('16:01 - 16:30', '16:01 - 16:30'),
    ('16:31 - 17:00', '16:31 - 17:00'),
    ('17:01 - 17:30', '17:01 - 17:30'),
    ('17:31 - 18:00', '17:31 - 18:00'),
)

DAY_CHOICES = (
    ('Monday', 'MONDAY'),
    ('Tuesday', 'TUESDAY'),
    ('Wednesday', 'WEDNESDAY'),
    ('Thursday', 'THURSDAY'),
    ('Friday', 'FRIDAY'),
    ('Saturday', 'SATURDAY'),
    ('Sunday', 'SUNDAY'),
)

class UserDetails(models.Model):
    Name = models.CharField(max_length=100, help_text='Probably your name.')
    Service = models.CharField(max_length=255,choices=SERVICES,help_text="")
    Time = models.CharField(max_length=13,choices=TIME_CHOICES,default='09:00',help_text='Please select a time in 24hr clock format (HH:MM) from the drop down.')
    Email = models.EmailField(max_length=254,help_text='Please provide email in case of cancellation.')
    Day = models.CharField(max_length=9,choices=DAY_CHOICES, default='MONDAY')
    

    def __str__(self):
        return self.Name
