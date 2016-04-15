from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Customer(models.Model):
    number = models.IntegerField(_("number"), null=True, blank=True, unique=True)
    name = models.CharField(_("name"), max_length=45)
    sex = models.CharField(_("sex"), max_length=6, null=True, blank=True)
    age = models.IntegerField(_("age"), null=True, blank=True)
    born = models.DateField(_("born"), null=True, blank=True)
    address = models.CharField(_("address"), max_length=255, null=True, blank=True)
    cellphone = models.CharField(_("cellphone"), max_length=20, null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=20, null=True, blank=True)
    user = models.OneToOneField('auth.User', related_name='customer', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = '顧客資料'
        verbose_name_plural = '顧客資料'

    def __str__(self):
        return self.name


class Master(models.Model):
    number = models.IntegerField(_("number"), null=True, blank=True, unique=True)
    name = models.CharField(_("name"), max_length=45)
    sex = models.CharField(_("sex"), max_length=6, null=True, blank=True)
    cellphone = models.CharField(_("cellphone"), max_length=20, null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=20, null=True, blank=True)
    user = models.OneToOneField('auth.User', related_name='master', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "師傅資料"
        verbose_name_plural = "師傅資料"

    def __str__(self):
        return self.name
