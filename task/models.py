from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class HourSlot(models.Model):
    name = models.CharField(max_length=20)
    order = models.IntegerField(default=50,unique=True)
    is_active = models.BooleanField(
        _('is_active'),
        default=True,
        help_text=_(
            'Unselect this instead of deleting HourSlot.'
        ),
    )
    def __str__(self):
        return self.name

class WeekDay(models.Model):
    name = models.CharField(max_length=20)
    order = models.IntegerField(default=50,unique=True)
    #max_patients = models.IntegerField(default=50)
    code = models.IntegerField(default=50,unique=True)
    is_active = models.BooleanField(
        _('is_active'),
        default=True,
        help_text=_(
            'Unselect this instead of deleting WeekDay.'
        ),
    )
    def __str__(self):
        return self.name
class Doctor(models.Model):#
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class DoctorDay(models.Model):#el 3yada  
    doctor = models.ForeignKey(Doctor,on_delete=models.PROTECT,related_name="DoctorDay_doctor",)
    day = models.ForeignKey(WeekDay,on_delete=models.PROTECT,related_name="DoctorDay_day",)
    class Meta:
        unique_together = ('doctor', 'day')
    def __str__(self):
        return "{}-{}".format(self.doctor.name,str(self.day.name))


class DoctorDaySlot(models.Model):
    doctor_day = models.ForeignKey(DoctorDay,on_delete=models.CASCADE,related_name="DoctorDaySlot_day",)
    slot = models.ForeignKey(HourSlot,on_delete=models.CASCADE,related_name="DoctorDay_slot",)
    class Meta:
        unique_together = ('doctor_day', 'slot')