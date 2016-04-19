from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Reservation(models.Model):
    customer = models.ForeignKey('user.Customer', verbose_name=_("customer"), related_name="reservation",
                                 on_delete=models.CASCADE)
    master = models.ForeignKey('user.Master', verbose_name=_("master"), related_name="reservation",
                               on_delete=models.CASCADE)
    date = models.DateField(_("date"))
    start_time = models.TimeField(_('start time'), choices=(
        (datetime.strptime('8:00', "%H:%M").time(), '8:00'),
        (datetime.strptime('8:30', "%H:%M").time(), '8:30'),
        (datetime.strptime('9:00', "%H:%M").time(), '9:00'),
        (datetime.strptime('9:30', "%H:%M").time(), '9:30'),
        (datetime.strptime('10:00', "%H:%M").time(), '10:00'),
        (datetime.strptime('10:30', "%H:%M").time(), '10:30'),
        (datetime.strptime('11:00', "%H:%M").time(), '11:00'),
        (datetime.strptime('11:30', "%H:%M").time(), '11:30'),
        (datetime.strptime('12:00', "%H:%M").time(), '12:00'),
        (datetime.strptime('12:30', "%H:%M").time(), '12:30'),
        (datetime.strptime('13:00', "%H:%M").time(), '13:00'),
        (datetime.strptime('13:30', "%H:%M").time(), '13:30'),
        (datetime.strptime('14:00', "%H:%M").time(), '14:00'),
        (datetime.strptime('14:30', "%H:%M").time(), '14:30'),
        (datetime.strptime('15:00', "%H:%M").time(), '15:00'),
        (datetime.strptime('15:30', "%H:%M").time(), '15:30'),
        (datetime.strptime('16:00', "%H:%M").time(), '16:00'),
        (datetime.strptime('16:30', "%H:%M").time(), '16:30'),
        (datetime.strptime('17:00', "%H:%M").time(), '17:00'),
        (datetime.strptime('17:30', "%H:%M").time(), '17:30'),
        (datetime.strptime('18:00', "%H:%M").time(), '18:00'),
        (datetime.strptime('18:30', "%H:%M").time(), '18:30'),
        (datetime.strptime('19:00', "%H:%M").time(), '19:00'),
        (datetime.strptime('19:30', "%H:%M").time(), '19:30'),
        (datetime.strptime('20:00', "%H:%M").time(), '20:00'),
        (datetime.strptime('20:30', "%H:%M").time(), '20:30'),
        (datetime.strptime('21:00', "%H:%M").time(), '21:00'),
        (datetime.strptime('21:30', "%H:%M").time(), '21:30'),
        (datetime.strptime('22:00', "%H:%M").time(), '22:00'),
        (datetime.strptime('22:30', "%H:%M").time(), '22:30'),
    ))
    hour = models.FloatField(_("hour"), choices=((0.5, 0.5), (1, 1), (1.5, 1.5), (2.0, 2.0)))
    category = models.CharField(_('massage category'), null=True, blank=True, max_length=20)
    remark = models.TextField(_("remark"), null=True, blank=True)
