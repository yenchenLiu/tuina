from django.forms import ModelForm, TextInput
from django.contrib import admin
from django.utils.translation import ugettext as _
from django import forms

from suit.widgets import AutosizedTextarea

from user.models import Customer, Master
from medical_record.models import Complaint


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('customer', 'number', 'massage_times', 'chief_complaint', 'timestamp')

    fieldsets = [
        ('主訴人', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['customer']
        }),
        ('主訴資料', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['number', 'massage_times', 'chief_complaint']}),

    ]

    suit_form_tabs = (('general', '一般資料'),)


admin.site.register(Complaint, ComplaintAdmin)



