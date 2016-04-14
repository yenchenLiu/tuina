from django.forms import ModelForm, TextInput
from django.contrib import admin
from django.utils.translation import ugettext as _
from django import forms
from consumer.models import MembershipCard, ExpensesRecord


class ExpensesRecordInline(admin.StackedInline):
    model = ExpensesRecord
    extra = 1
    can_delete = False
    fieldsets = [('', {
        'classes': ('suit-tab', 'suit-tab-expense',),
        'fields': ['hour', 'category', 'datetime']
    }),
    ]


class MembershipCardAdmin(admin.ModelAdmin):
    inlines = (ExpensesRecordInline,)
    list_display = (
        'customer', 'number', 'category', 'remaining_time', 'payment_method', 'total_money', 'amount_paid', 'remark')
    search_fields = ('customer__name', 'number')

    def remaining_time(self, obj):
        remaining_time = obj.hour
        for item in obj.expenses_record.all():
            remaining_time -= item.hour
        return str(remaining_time) + "小時"

    remaining_time.short_description = _("remaining time")
    readonly_fields = ['remaining_time']
    fieldsets = [
        ('持有人', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['customer', 'remaining_time'],
        }),
        ('卡片資料', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['number', 'category', 'hour', 'total_money', 'payment_method', 'amount_paid',
                       'remark']}),

    ]
    suit_form_tabs = (('general', '一般資料'), ("expense", "消費資料"))

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.customer = form.instance.customer
            instance.MembershipCard = form.instance
            instance.save()
        formset.save_m2m()

    def suit_row_attributes(self, obj, request):
        return {'class': 'font-size-large'}

    def suit_cell_attributes(self, obj, column):
        return {'class': 'font-size-large'}


admin.site.register(MembershipCard, MembershipCardAdmin)


class ExpensesRecordAdmin(admin.ModelAdmin):
    list_display = ('customer', 'id', 'membership_card', 'price', 'hour', 'category', 'datetime')
    search_fields = ('customer__name', 'id', 'membership_card__number')
    fieldsets = [
        ('顧客資料', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['customer', 'price']
        }),
        ('服務資料', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['hour', 'category', 'datetime']}),

    ]

    suit_form_tabs = (('general', '一般資料'),)

    def suit_row_attributes(self, obj, request):
        return {'class': 'font-size-large'}

    def suit_cell_attributes(self, obj, column):
        return {'class': 'font-size-large'}


admin.site.register(ExpensesRecord, ExpensesRecordAdmin)
