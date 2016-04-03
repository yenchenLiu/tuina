from django.db import models
from user.models import Customer
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Complaint(models.Model):
    number = models.IntegerField(_("number"), null=True, blank=True, unique=True)
    massage_times = models.IntegerField(_("massage times"), null=True, blank=True)
    chief_complaint = models.TextField(_("chief complaint"), null=True, blank=True)
    timestamp = models.DateTimeField(_("timestamp"), auto_now=True)
    customer = models.ForeignKey('user.Customer', verbose_name=_("customer"), related_name="complaint",
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = "主訴資料"
        verbose_name_plural = "主訴資料"
