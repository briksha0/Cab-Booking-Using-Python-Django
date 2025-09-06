from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *

# admin.site.register(page2)
# admin.site.register(PAGE3HEADING)
# admin.site.register(page3)
# admin.site.register(page4)
# admin.site.register(PAGE5HEADING)
# admin.site.register(PAGE7HEADING)
# admin.site.register(PAGE5_PARA)
# admin.site.register(PAGE5_IMG)
# admin.site.register(page7img)
# admin.site.register(page7info)
# admin.site.register(cabEnquiry)
# admin.site.register(Payment)

# admin.site.register(Carstype)
# admin.site.register(Tempo)
# admin.site.register(TermsAndConditions)


# admin.site.register(PickupLocation)
# admin.site.register(Droplocation)
# admin.site.register(ContactUsFormData)
# admin.site.register(ReservationFormData)

class Damadmin(ImportExportModelAdmin):
    pass
admin.site.register(BookingCab,Damadmin)
