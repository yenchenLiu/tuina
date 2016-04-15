from django.forms import ModelForm, TextInput
from django.contrib import admin
from django.utils.translation import ugettext as _
from django import forms

from suit.widgets import AutosizedTextarea

from user.models import Customer, Master
from medical_record.models import Complaint
from consumer.models import MembershipCard


class ComplaintInline(admin.StackedInline):
    model = Complaint
    extra = 0
    suit_classes = 'suit-tab suit-tab-complaint'
    show_change_link = True
    readonly_fields = ['timestamp']


class MembershipCardInline(admin.StackedInline):
    model = MembershipCard
    extra = 0
    suit_classes = 'suit-tab suit-tab-member'
    show_change_link = True

    def remaining_time(self, obj):
        remaining_time = obj.hour
        for item in obj.expenses_record.all():
            remaining_time -= item.hour
        return str(remaining_time) + "小時"

    remaining_time.short_description = _("remaining time")
    readonly_fields = ['remaining_time']


class CustomerAdmin(admin.ModelAdmin):
    inlines = (ComplaintInline, MembershipCardInline)

    list_display = ('name', 'number', 'sex', 'age', 'phone', 'cellphone')
    search_fields = ('number', 'name', 'phone', 'cellphone')

    fieldsets = [
        ('基本資料', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['number', 'name', 'sex', 'born']
        }),
        ('聯絡資料', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['address', 'phone', 'cellphone']}),
        ('帳戶', {
            'classes': ('suit-tab', 'suit-tab-user',),
            'fields': ['user']}),

    ]

    suit_form_tabs = (
        ('general', '一般資料'), ('user', '進階資料'), ('complaint', _("chief complaint")), ('member', _("member card")))

    def suit_row_attributes(self, obj, request):
        return {'class': 'font-size-large'}

    def suit_cell_attributes(self, obj, column):
        return {'class': 'font-size-large'}


class CustomerForm(ModelForm):
    class Meta:
        widgets = {
            'name': TextInput(attrs={'class': 'input-mini'})
        }


admin.site.register(Customer, CustomerAdmin)


class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'sex', 'phone', 'cellphone')
    search_fields = ('number', 'name', 'phone', 'cellphone')

    fieldsets = [
        ('基本資料', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['number', 'name', 'sex']
        }),
        ('聯絡資料', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['phone', 'cellphone']}),
        ('帳戶', {
            'classes': ('suit-tab', 'suit-tab-user',),
            'fields': ['user']}),
    ]

    suit_form_tabs = (('general', '一般資料'), ('user', '進階資料'))

    def suit_row_attributes(self, obj, request):
        return {'class': 'font-size-large'}

    def suit_cell_attributes(self, obj, column):
        return {'class': 'font-size-large'}


admin.site.register(Master, MasterAdmin)
