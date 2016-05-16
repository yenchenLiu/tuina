import datetime

from django.contrib import admin
from django import forms
from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
from reservation.models import Reservation, PhoneRecord
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _


# Register your models here.


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('customer', 'date', 'start_time', 'hour',
                  'category', 'master', 'remark')

        widgets = {
            'date': SuitDateWidget,
        }

    def clean(self):
        try:
            start_time = self.cleaned_data["start_time"].hour
            if self.cleaned_data["start_time"].minute == 30:
                start_time += 0.5
            end_time = start_time + self.cleaned_data["hour"]

            reservation_list = Reservation.objects.filter(
                master=self.cleaned_data['master'],
                date=self.cleaned_data['date']
            ).exclude(id=self.instance.id)
            for item in reservation_list:
                start = item.start_time.hour

                if item.start_time.minute == 30:
                    start += 0.5
                min_hour = start
                max_hour = start + item.hour

                if min_hour <= start_time < max_hour:
                    raise forms.ValidationError("時間重疊")
                elif min_hour <= end_time < max_hour:
                    raise forms.ValidationError("時間重疊")
                elif start_time <= min_hour <= end_time:
                    raise forms.ValidationError("時間重疊")

        except Exception as e:
            raise e

        return self.cleaned_data


class ReservationAdmin(admin.ModelAdmin):
    form = ReservationForm
    list_display = ('customer', 'date', 'start_time', 'hour',
                    'category', 'master', 'remark')
    search_fields = ('number', 'customer__name', 'chief_complaint')

    suit_form_tabs = (('general', '一般資料'),)

    def suit_row_attributes(self, obj, request):
        return {'class': 'font-size-large'}

    def suit_cell_attributes(self, obj, column):
        return {'class': 'font-size-large'}


admin.site.register(Reservation, ReservationAdmin)


class PhoneRecordAdmin(admin.ModelAdmin):
    list_display = ('phone', 'datetime', 'remark')
    search_fields = ('phone__phone_number', 'remark')

    suit_form_tabs = (('general', '一般資料'),)

    def suit_row_attributes(self, obj, request):
        return {'class': 'font-size-large'}

    def suit_cell_attributes(self, obj, column):
        return {'class': 'font-size-large'}


admin.site.register(PhoneRecord, PhoneRecordAdmin)

