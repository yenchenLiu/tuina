from django.shortcuts import render
from reservation.models import Reservation
from reservation import templateFilter
from user.models import Master
# Create your views here.


def reservation_condition(request):
    context = {"master": []}
    master = Master.objects.all()
    for item in master:
        data = {"name": item.name, "data": Reservation.objects.filter(master=item)}
        context["master"].append(data)
    print(context)
    return render(request, "reservation/timeline.html", context)
