import datetime

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from .models import PhoneRecord
from user.models import CustomerPhone
from user.models import Master
from reservation.models import Reservation
from reservation import templateFilter


# Create your views here.


def reservation_condition(request):
    context = {"master": []}
    master = Master.objects.all()
    for item in master:
        data = {"name": item.name, "data": Reservation.objects.filter(master=item)}
        context["master"].append(data)
    return render(request, "reservation/timeline.html", context)


class PhoneLog(View):
    def get(self, request, *args, **kwargs):
        if 'phone' in kwargs:
            return self.call_in(request, *args, **kwargs)
        context = {}
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        phone_list = PhoneRecord.objects.filter(datetime__range=(today_min, today_max)).order_by("-id")
        context["phone_list"] = phone_list
        return render(request, "phone/phone_log.html", context)

    def call_in(self, request, *args, **kwargs):
        try:
            phone = CustomerPhone.objects.get(phone_number=kwargs["phone"])
        except ObjectDoesNotExist:
            phone = CustomerPhone.objects.create(phone_number=kwargs["phone"])
        PhoneRecord.objects.create(phone=phone)
        return redirect(reverse("phone_log"))


class CustomerPhoneLog(View):
    def get(self, request, *args, **kwargs):
        profile_id = kwargs["profile_id"]
        context = {}
        phone_list = PhoneRecord.objects.filter(phone__customer__id=profile_id).order_by("-id")[:10]
        context["phone_list"] = phone_list
        return render(request, "phone/phone_log.html", context)
