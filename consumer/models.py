from django.db import models
from user.models import Customer
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class MembershipCard(models.Model):
    number = models.IntegerField(_("number"), unique=True)
    category = models.CharField(_("category"), max_length=45, choices=(
        ("一般", "一般"), ("深層推拿", "深層推拿")))
    hour = models.FloatField(_("hour"))
    total_money = models.IntegerField(_("total money"))
    payment_method = models.CharField(_("payment method"), max_length=20, choices=(("現金", "現金"), ("刷卡", "刷卡")))
    amount_paid = models.IntegerField(_("amount paid"), default=0)
    remark = models.TextField(_("remark"), null=True, blank=True)
    customer = models.ForeignKey('user.Customer', verbose_name=_("customer"), related_name="membership_card",
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = '會員卡資料'
        verbose_name_plural = '會員卡資料'

    def __str__(self):
        return str(self.number)


class ExpensesRecord(models.Model):
    hour = models.FloatField(_("hour"))
    price = models.IntegerField(_("price"), null=True, blank=True)
    category = models.CharField(_("category"), max_length=45, choices=(
        ("一般", "一般"), ("深層推拿", "深層推拿")))
    datetime = models.DateTimeField(_("datetime"))
    customer = models.ForeignKey('user.Customer', verbose_name=_("customer"), related_name="expenses_record",
                                 on_delete=models.CASCADE)
    membership_card = models.ForeignKey('MembershipCard', verbose_name=_("membership card"),
                                        related_name="expenses_record", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = '消費資料'
        verbose_name_plural = '消費資料'

    def __str__(self):
        return str(self.id)
