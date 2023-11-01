from django.contrib import admin

from .models import Owner, Building, Room, Organization, Subdivision, Responsible, WireCore, Equipment, Port, Cable

admin.site.register(Owner)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Organization)
admin.site.register(Subdivision)
admin.site.register(Responsible)
admin.site.register(WireCore)
admin.site.register(Equipment)
admin.site.register(Port)
admin.site.register(Cable)
