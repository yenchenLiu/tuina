from django.contrib import admin
from django import forms
from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
from reservation.models import Reservation
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
            'start_time': SuitTimeWidget,
        }


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
