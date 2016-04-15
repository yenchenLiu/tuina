from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Reservation(models.Model):
    customer = models.ForeignKey('user.Customer', verbose_name=_("customer"), related_name="reservation",
                                 on_delete=models.CASCADE)
    master = models.ForeignKey('user.Master', verbose_name=_("master"), related_name="reservation",
                               on_delete=models.CASCADE)
    date = models.DateField(_("date"))
    start_time = models.TimeField(_('start time'))
    hour = models.FloatField(_("hour"), choices=((0.5, 0.5), (1, 1), (1.5, 1.5), (2.0, 2.0)))
    category = models.CharField(_('massage category'), null=True, blank=True, max_length=20)
    remark = models.TextField(_("remark"), null=True, blank=True)
