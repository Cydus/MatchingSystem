from django.contrib import admin
from models import Project, Position, Application, Offer

#admin.site.register(Project)
admin.site.register(Position)
admin.site.register(Application)
admin.site.register(Offer)

class ProjectAdmin(admin.ModelAdmin):
        list_display = ('name', 'description')

admin.site.register(Project, ProjectAdmin)
