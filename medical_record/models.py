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

    def __str__(self):
        return str(self.timestamp)


class Lifestyle(models.Model):
    focus = models.CharField(_("life focus"), null=True, blank=True, max_length=20)
    physique = models.CharField(_("physique"), null=True, blank=True, max_length=20)
    sleep = models.CharField(_("sleep quality"), null=True, blank=True, max_length=20)
    diet = models.CharField(_("diet"), null=True, blank=True, max_length=20)
    excretion = models.CharField(_("excretion"), null=True, blank=True, max_length=20)
    remark = models.TextField(_("remark"), null=True, blank=True)
    complaint = models.OneToOneField('Complaint', verbose_name=_("complaint"), related_name="lifestyle",
                                     on_delete=models.CASCADE)


class Sport(models.Model):
    item = models.CharField(_("sport item"), null=True, blank=True, max_length=50)
    name = models.CharField(_("spot name"), null=True, blank=True, max_length=20)
    frequency = models.CharField(_("frequency"), null=True, blank=True, max_length=20)
    time = models.CharField(_("frequency time"), null=True, blank=True, max_length=20)
    history = models.CharField(_("history"), null=True, blank=True, max_length=20)
    review = models.CharField(_("review"), null=True, blank=True, max_length=20)
    remark = models.TextField(_("remark"), null=True, blank=True)
    complaint = models.OneToOneField('Complaint', verbose_name=_("sport"), related_name="sport",
                                     on_delete=models.CASCADE)


class Physique(models.Model):
    item = models.CharField(_("physique item"), null=True, blank=True, max_length=50)
    name = models.CharField(_("physique name"), null=True, blank=True, max_length=20)
    history = models.CharField(_("history"), null=True, blank=True, max_length=20)
    situation = models.CharField(_("situation"), null=True, blank=True, max_length=20)
    rehabilitation = models.CharField(_("rehabilitation"), null=True, blank=True, max_length=20)
    remark = models.TextField(_("remark"), null=True, blank=True)
    complaint = models.OneToOneField('Complaint', verbose_name=_("physique"), related_name="physique",
                                     on_delete=models.CASCADE)


class Massage(models.Model):
    customer = models.ForeignKey('user.Customer', verbose_name=_("customer"), related_name="massage",
                                 on_delete=models.CASCADE)
    master = models.ForeignKey('user.Master', verbose_name=_("master"), related_name="massage",
                               on_delete=models.CASCADE)
    massage_times = models.IntegerField(_("massage times"), null=True, blank=True)
    datetime = models.DateTimeField(_('datetime'))
    category = models.CharField(_('massage category'), null=True, blank=True, max_length=20)
    hour = models.FloatField(_("hour"))
    skill = models.CharField(_('massage skill'), null=True, blank=True, max_length=20)
    feel = models.CharField(_('massage feel'), null=True, blank=True, max_length=20)
    felt = models.CharField(_('massage felt'), null=True, blank=True, max_length=20)
    remark = models.TextField(_("remark"), null=True, blank=True)

    class Meta:
        verbose_name = "推拿資料"
        verbose_name_plural = "推拿資料"

    def __str__(self):
        return str(self.id)
