from django.contrib import admin
from ordrin.models import Sighting

class SightingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sighting, SightingAdmin)