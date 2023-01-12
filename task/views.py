# Create your views here.
import json
from django.shortcuts import render

from task.models import *
from rest_framework.views import APIView
from django.http import HttpResponseBadRequest, JsonResponse

def index(request):
    return render (request,'table/index.html') 


class DoctorApi(APIView):
    def get_object(self,pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return None    
    
    def get(self,request):
        pk= 1
        doctor=self.get_object(pk)
        if doctor :
            weekDays = WeekDay.objects.all().order_by('order').values()
            hourSlots = HourSlot.objects.filter(is_active=True).values().order_by('order')
            doctorDays = DoctorDay.objects.filter(doctor_id = pk).values('id' , 'day')
            doctor_workdays_ids = doctorDays.values_list('day',flat=True)#el ayam
            doctorDays_ids = doctorDays.values_list('id',flat=True)# ids of days
            doctorDaySlot_ids = DoctorDaySlot.objects.filter(doctor_day_id__in =doctorDays_ids).values_list('slot',flat=True)
            #for wd in weekDays : wd["is_working"] = True if wd["id"] in doctor_workdays_ids else False
            doctor_data_days =[]
            for wd in weekDays :
                obj={}
                doctor_day  =  doctorDays.filter(day_id=wd["id"])
                if doctor_day : doctor_day_id = doctor_day.first()['id']
                else : doctor_day_id = 0
                obj["day"] ={"id":wd["id"],"name":wd["name"],"is_working":True if wd["id"] in doctor_workdays_ids else False}
                obj["slots"]=[]
                doctorDaySlot_ids_day = doctorDaySlot_ids.filter(doctor_day_id= doctor_day_id)
                for hS in hourSlots :
                    slotObj ={"id":hS["id"] ,"is_working": True if hS["id"] in doctorDaySlot_ids_day else False }
                    obj["slots"].append(slotObj)
                doctor_data_days.append(obj)
        
            #doctorDaysSlots = DoctorDaySlot.objects.filter(doctor_id = pk).values('id' , 'day')
            #DoctorDaySlot.objects.filter(id)
            return render(request,'table/index.html',{
                        "doctor":doctor,
                        "doctor_data_days":doctor_data_days,
                        "hourSlots":hourSlots,
                        'activePage':'Doctors'})

       
    def post(self,request):
           if request.method == 'POST':
                data = json.load(request)
                checked = data.get('checked')
                weekDays = WeekDay.objects.all().values()
                DoctorDay.objects.filter(doctor_id=1).delete()
                days_index=[]
                for wd in weekDays :
                  for checkday in checked:
                    day_id=wd["id"]  
                    if wd["name"]==checkday:
                        days_index.append(int(checked.index(checkday)))                    
                        DoctorDay.objects.create(doctor_id=1,day_id=day_id)
                        checked[checked.index(checkday)]=day_id
                days_index.append(len(checked))
                for i in range(len(days_index)-1):
                   day_slots=checked[days_index[i]:days_index[i+1]]
                   doctor_day=DoctorDay.objects.filter(day_id=day_slots[0]).get()
                   for i in range(len(day_slots)-1):
                      DoctorDaySlot.objects.create(doctor_day_id=doctor_day.id,slot_id=day_slots[i+1])  
                return JsonResponse({'status': 'checked!'})
            
