from django.forms import ModelForm, TextInput
from django.contrib import admin
from medical_record.models import Complaint, Lifestyle, Sport, Physique, Massage


class LifestyleInline(admin.StackedInline):
    model = Lifestyle
    extra = 1
    suit_classes = 'suit-tab suit-tab-general'


class SportInline(admin.StackedInline):
    model = Sport
    extra = 1
    suit_classes = 'suit-tab suit-tab-general'


class PhysiqueInline(admin.StackedInline):
    model = Physique
    extra = 1
    suit_classes = 'suit-tab suit-tab-general'


class ComplaintAdmin(admin.ModelAdmin):
    inlines = (LifestyleInline, SportInline, PhysiqueInline)
    list_display = ('customer', 'number', 'massage_times', 'chief_complaint', 'timestamp')
    search_fields = ('number', 'customer__name', 'chief_complaint')
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

    def suit_row_attributes(self, obj, request):
        return {'class': 'font-size-large'}

    def suit_cell_attributes(self, obj, column):
        return {'class': 'font-size-large'}


admin.site.register(Complaint, ComplaintAdmin)


class MassageAdmin(admin.ModelAdmin):
    list_display = ('customer', 'massage_times', 'datetime', 'category',
                    'hour', 'master', 'skill', 'feel', 'felt', 'remark')
    search_fields = ('master__name', 'customer__name')
    # fieldsets = [
    #     ('主訴人', {
    #         'classes': ('suit-tab', 'suit-tab-general',),
    #         'fields': ['customer']
    #     }),
    #
    # ]

    suit_form_tabs = (('general', '一般資料'),)

    def suit_row_attributes(self, obj, request):
        return {'class': 'font-size-large'}

    def suit_cell_attributes(self, obj, column):
        return {'class': 'font-size-large'}


admin.site.register(Massage, MassageAdmin)
