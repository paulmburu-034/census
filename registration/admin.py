from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import RegistrationCentre


class RegistrationCentreAdmin(admin.ModelAdmin):
    list_display = ('reg_centre_name', 'reg_centre_county')
    list_filter = ('reg_centre_name',)
    search_fields = ('reg_centre_name', 'reg_centre_county', 'reg_centre_type')


admin.site.register(RegistrationCentre, RegistrationCentreAdmin)

