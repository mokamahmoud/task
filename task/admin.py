from django.contrib import admin
from task.models import *
# Register your models here.

admin.site.register(Doctor)

class HourSlotAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')

admin.site.register(HourSlot, HourSlotAdmin)

class WeekDayAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'order',"code")

admin.site.register(WeekDay, WeekDayAdmin)


class DoctorDayAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day')
    ordering = ["doctor","day"]
admin.site.register(DoctorDay, DoctorDayAdmin)


class DoctorDaySlotAdmin(admin.ModelAdmin):
    list_display = ('doctor_day', 'slot')

admin.site.register(DoctorDaySlot, DoctorDaySlotAdmin)